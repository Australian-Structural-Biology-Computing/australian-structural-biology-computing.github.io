---
title: Welcome
toc: false
# Special sidebar rules for news on the index page are included in layouts/default.html, as in https://github.com/workflowhub-eu/about/blob/596b18d7ab1055ee1e53bc98a3bd120a06518e06/_layouts/default.html
#hide_sidebar: true
#sidebar: true
redirect_from: /website/
tiles:
  - title: "Join the conversation"
    url: /join_conversation
  - title: "Read the Australian infrastructure roadmap"
    url: https://doi.org/10.5281/zenodo.15786982
---


This website is a virtual meeting place and hub for all users of **computing for structural biology research in Australia**. This is a collective community effort. It can be what we make it!

{% include tiles-simple.html target = "tiles" col = "2" %}

## Protein design seminar series

{% include video-list-columns.html 
   video_id="xwvF62HxaF0" 
   list="The protein design seminar series includes <b>5 presentations</b> from Australian structural biologists utilising the latest developments in <i>de novo</i> protein design to develop protein binders to various therapeutic targets.|Watch <b>Dr Josh Hardy</b> share a recent project describing the development of  ProteinDJ: A modular and open-source framework for protein design workflows.|The full series schedule, seminar registration link and recordings of completed seminars are available <b><a href=\"/protein_design_seminars\">here</a></b>.|The final event in the series will be on <b>November 11th</b> and will describe baby steps in the AI-guided design of proteins to modulate gene transcription." %}

## Upcoming Events

{% include events.html event_type="upcoming_event" limit=4 %}


## Acknowledgements

This website represents a joint effort by many people at multiple Australian institutions. 
A list of contributors is [available here](contributors).

{% include affiliation-tiles-selection.html %}
