---
title: Welcome
toc: false
# Special sidebar rules for news on the index page are included in layouts/default.html, as in https://github.com/workflowhub-eu/about/blob/596b18d7ab1055ee1e53bc98a3bd120a06518e06/_layouts/default.html
#hide_sidebar: true
#sidebar: true

tiles:
  - title: "Join the conversation"
    url: /join_conversation
---


This website is a virtual meeting place and hub for all users of **computing for structural biology research in Australia**. This is a collective community effort. It can be what we make it!

{% include tiles-simple.html target = "tiles" col = "2" %}


## Upcoming Events

{% include events.html event_type="upcoming_event" limit=4 %}


## Acknowledgements

This website represents a joint effort by many people at multiple Australian institutions. 
A list of contributors is [available here](contributors).

{% include affiliation-tiles-selection.html %}
