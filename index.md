---
layout: landing
title: Australian Structural Biology Computing
hero_title: A community resource
summary: Discover shared resources, current activities, community meetings and ways to contribute.
hero_actions:
  - title: Join the community
    url: /join_conversation
    style: btn-light
  - title: Explore activities
    url: /activities
    style: btn-outline-light
  - title: Contribute your work
    url: /contributing
    style: btn-outline-light
  - title: Infrastructure roadmap
    url: https://doi.org/10.5281/zenodo.15786982
    style: btn-outline-light
toc: false
sidebar: false
redirect_from: /website/
resource_tiles:
  - title: Community resources
    url: /community_resources
    description: Resources developed and recommended by the ASBC community.
  - title: How-to guides
    url: /guides
    description: Practical guidance for structural biology computing tasks.
  - title: Computational workflows
    url: /workflows
    description: Reusable workflows for structural biology research.
  - title: Software
    url: /software
    description: Software shared by and useful to the community.
  - title: Resource library
    url: /library
    description: Browse the complete collection of tools and resources.
  - title: External resources
    url: /external_resources
    description: Explore specialist tools, services and infrastructure.
---

## Explore resources

{% include tiles-simple.html target="resource_tiles" col=3 %}

{% include events.html event_type="upcoming_event" title=true caption=true col=2 %}

## News

{% include news.html limit=2 caption=true %}

## Acknowledgements

This community represents a joint effort by people at multiple Australian institutions. 
A list of contributors is [available here](contributors).

{% include affiliation-tiles-selection.html %}
