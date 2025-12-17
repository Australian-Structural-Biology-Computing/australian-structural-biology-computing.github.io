---
title: Welcome
toc: false
# Special sidebar rules for news on the index page are included in layouts/default.html, as in https://github.com/workflowhub-eu/about/blob/596b18d7ab1055ee1e53bc98a3bd120a06518e06/_layouts/default.html
#hide_sidebar: true
#sidebar: true
redirect_from: /website/
tiles:
  - title: "Join the mailing list, meetings etc."
    url: /join_conversation
  - title: "See activities that are in progress"
    url: /activities
  - title: "Share your work with the community"
    url: /contributing
---


This website is a virtual meeting place and hub for all users of **computing for structural biology research in Australia**. This is a collective community effort. It can be what we make it!

## Getting involved

{% include tiles-simple.html target = "tiles" col = "3" %}


## Protein design seminar series - watch the recordings

| Speaker    | Topic & link to YouTube |
|--------------------|------------------------------------------------------------------------------|----------|
| Rhys Grinter       | [Using AI protein design to design binding proteins to challenging bacterial transporters](https://youtu.be/3Ad2gUjeSL8)  |
| Cyntia Taveneau    | [AIcrs: AI-Designed Anti-CRISPRs as Programmable CRISPR Inhibitors](https://www.youtube.com/watch?v=GSoOfyJUYSA)   |
| Richard Birkinshaw | [Using in silico design methods to create *de novo* proteins that selectively modulate apoptosis](https://youtu.be/9-3sHy1ybpE)      |
| Josh Hardy | [Introducing ProteinDJ: A modular and open-source framework for protein design workflows](https://www.youtube.com/watch?v=xwvF62HxaF0) | 
| Joel Mackay | [Baby steps in the AI-guided design of proteins to modulate gene transcription](https://www.youtube.com/watch?v=tKqH8WlkIX4)         | 


## Upcoming Events

{% include events.html event_type="upcoming_event" limit=4 %}


## Acknowledgements

This website represents a joint effort by many people at multiple Australian institutions. 
A list of contributors is [available here](contributors).

{% include affiliation-tiles-selection.html %}
