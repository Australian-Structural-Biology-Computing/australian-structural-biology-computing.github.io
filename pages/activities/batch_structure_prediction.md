---
title: Batch structure prediction workflows
description: Developing optimized batch workflows for structure prediction.
type: Activity_in_progress
roadmap: A shared platform, or platforms (Roadmap D3A)
roadmap_category: Shared-platform
contributors: [Ziad Al-Bkhetan, Mitchell O'Brien, Joshua Storm Caley, Keiran Rowell, Cameron Hyde, Thomas Litfin]
toc: false
redirect_from: /website/batch_structure_prediction
tiles:
  - title: Explore the WISPS interaction-screening workflow
    url: https://github.com/Australian-Structural-Biology-Computing/wisps
---

{% include tiles-simple.html target="tiles" col="1" variant="simple" %}

## Details

- Structure prediction software often natively supports single predictions.
- Specific workflows can re-use MSA input to massively improve efficiency over naive implementation. For example, interaction screening where 1 protein is predicted in combination with many others.

This activity involves developing optimized batch workflows for structure prediction.

### Completed

- Add support for re-using MSAs to Galaxy Australia AlphaFold2 service.
- Add local implementation of batch colabfoldsearch to the [nf-core/proteinfold](https://nf-co.re/proteinfold/2.0.0/) pipeline.
- Develop the [WISPS](https://github.com/Australian-Structural-Biology-Computing/wisps) interaction-screening workflow.

