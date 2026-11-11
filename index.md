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
    style: btn-hero-accent
  - title: Contribute your work
    url: /contributing
    style: btn-outline-light
  - title: Infrastructure roadmap
    url: https://doi.org/10.5281/zenodo.15786982
    style: btn-hero-warm
toc: false
sidebar: main
redirect_from: /website/
---

{% include events.html event_type="upcoming_event" title=true caption=true col=2 %}

<section class="landing-news">
  <h2>News</h2>

{% include news.html limit=2 caption=true %}
</section>

<section class="landing-contributors" aria-labelledby="contributors-heading">
  <div class="d-flex flex-wrap align-items-baseline justify-content-between gap-2 mb-3">
    <div>
      <h2 id="contributors-heading" class="mb-2">Community contributors</h2>
      <p class="mb-0">Meet the people sharing expertise, resources and infrastructure across the community.</p>
    </div>
    <a href="{{ '/community_contributors' | relative_url }}">View all contributors</a>
  </div>

{% include contributor-carousel-selection.html %}
</section>

<section class="landing-acknowledgements">
  <h2>Acknowledgements</h2>
  <p>This community represents a joint effort by people at multiple Australian institutions. Meet the <a href="/academic_panel">Academic Panel</a> and our <a href="/community_contributors">Community Contributors</a>.</p>

{% include affiliation-tiles-selection.html %}
</section>
