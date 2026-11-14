---
title: Community access to protein design
description: Improving access to open protein-design workflows and preparing them for delivery through national infrastructure.
type: Activity_in_progress
roadmap: A shared platform, or platforms (Roadmap D3Ac)
roadmap_category: Shared-platform
contributors: [Ziad Al-Bkhetan, Thomas Litfin]
toc: false
redirect_from: /website/bindcraft_access
tiles:
  - title: Read how ProteinDJ removed restricted dependencies
    url: https://www.biocommons.org.au/news/proteindj-v3
  - title: Explore the ProteinDJ workflow
    url: https://github.com/PapenfussLab/proteindj
  - title: Follow the Structural Biology Platform
    url: https://www.biocommons.org.au/structural-biology-platform
---

{% include tiles-simple.html target="tiles" col="3" variant="simple" %}

## Details

- [BindCraft](https://github.com/martinpacesa/BindCraft) provides an end-to-end approach to designing protein binders, but its traditional workflow depends on PyRosetta and associated licence conditions.
- [ProteinDJ](https://github.com/PapenfussLab/proteindj) is a modular Nextflow pipeline that combines multiple protein-design methods and can run across computing environments.
- ProteinDJ v3 replaced its restricted components, including the PyRosetta-dependent path, with alternatives that support broader academic and commercial use.
- This work prepares ProteinDJ for inclusion in the Australian BioCommons Structural Biology Platform.


### Completed

- Wrap the BindCraft tool in a Nextflow workflow (**[bindflow](https://github.com/Australian-Structural-Biology-Computing/bindflow)**).
- Add support for parallel execution across multiple GPUs.
- Negotiate PyRosetta license for non-commercial use at NCI.
- Output partial results when HPC scheduler jobs time out.
- Contribute to ProteinDJ v3, replacing licence-restricted dependencies and improving performance and usability.
- Replace the BindCraft stage in ProteinDJ with FreeBindCraft and replace PyRosetta-based relaxation with a GPU-enabled alternative.


### In progress

- Prepare ProteinDJ for delivery through the Australian BioCommons Structural Biology Platform.
- Support the platform's planned public launch in Q1 2027, providing browser-based access to protein structure prediction and design workflows on sponsored computing resources.
