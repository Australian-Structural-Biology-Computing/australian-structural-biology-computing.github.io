# Compatibility implementation of the ELIXIR Toolkit Theme tool tag for this
# site's Jekyll 3 build. Based on elixir-toolkit-theme-plugins 0.1.10 (MIT).

require "cgi"
require "jekyll"
require "set"

module Jekyll
  class EttToolTag < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      super
      match = markup.match(/\A\s*["']([^"']+)["']\s*\z/)
      raise ArgumentError, 'Tool tags must use {% tool "tool-id" %}' unless match

      @tool_id = match[1]
    end

    def render(context)
      tools = context.registers[:site].data["tool_and_resource_list"] || []
      tool = tools.find { |item| item["id"] == @tool_id }
      raise ArgumentError, "Undefined tool ID: #{@tool_id}" unless tool

      name = CGI.escapeHTML(tool["name"].to_s)
      description = CGI.escapeHTML(tool["description"].to_s)
      tags = website_tag(tool["url"])

      %(<a tabindex="0" class="tool" role="button" aria-description="#{description}" ) +
        %(data-bs-toggle="popover" data-bs-placement="bottom" data-bs-trigger="focus" ) +
        %(data-bs-content="<h5>#{name}</h5><div class='mb-2'>#{description}</div>#{tags}" ) +
        %(data-bs-template="<div class='popover popover-tool' role='tooltip'><div class='popover-arrow'></div><h3 class='popover-header'></h3><div class='popover-body'></div></div>" ) +
        %(data-bs-html="true"><i class="fa-solid fa-wrench fa-sm me-2"></i>#{name}</a>)
    end

    private

    def website_tag(url)
      safe_url = CGI.escapeHTML(url.to_s)
      %(<a href='#{safe_url}' target='_blank' rel='noopener' class='mt-2 me-2'><span class='badge bg-dark text-white hover-primary'><i class='fa-solid fa-link me-2'></i>Website</span></a>)
    end
  end

  module EttToolTableFilter
    def add_related_pages(data)
      related_pages = Hash.new { |hash, key| hash[key] = Set.new }

      Dir.glob(File.join(Dir.pwd, "**", "*.md")).each do |path|
        content = File.read(path)
        page_id = content[/page_id:\s*(\w+)/, 1]
        next unless page_id

        content.scan(/\{%\s*tool\s*["']([^"']+)["']\s*%\}/).flatten.each do |tool_id|
          related_pages[tool_id].add(page_id)
        end
      end

      data.each do |tool|
        tool["related_pages"] = related_pages[tool["id"]].to_a if tool["id"] && related_pages.key?(tool["id"])
      end
      data
    end
  end
end

Liquid::Template.register_tag("tool", Jekyll::EttToolTag)
Liquid::Template.register_filter(Jekyll::EttToolTableFilter)
