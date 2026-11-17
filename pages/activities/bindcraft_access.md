---
title: Community access to BindCraft
description: Increasing community access to an end-to-end solution for protein binder design.
type: Completed_activity
roadmap: A shared platform, or platforms (Roadmap D3Ac)
roadmap_category: Shared-platform
contributors: [Ziad Al-Bkhetan, Thomas Litfin, Josh Hardy]
toc: false
redirect_from: /website/bindcraft_access
---


## Details

- [BindCraft](https://github.com/martinpacesa/BindCraft) is an end-to-end solution for protein binder design.
- BindCraft was widely used by participants in a recent blind evaluation ([Adaptyv Bio](https://www.adaptyvbio.com/blog/po104)) of protein binder design tools.
- Several independent groups generated *de novo* designed binders with competitive affinity to the natural ligand using the BindCraft tool.
- BindCraft tool is available within a NextFlow [workflow](https://github.com/Australian-Structural-Biology-Computing/bindflow) to support portable deployment.
- BindCraft is also available within the [ProteinDJ](https://github.com/PapenfussLab/proteindj) workflow developed by community members from the Lucet and Papenfuss labs at WEHI.

{% include callout.html type="warning" content="Native BindCraft tool requires PyRosetta as a filter with non-commercial license." %}

- ProteinDJ v3 was developed to remove PyRosetta as a dependency (see [ProteinDJ v3.0 release](proteindj_v3)).


### Completed

- Wrap the BindCraft tool in a Nextflow workflow ([**bindflow**](https://github.com/Australian-Structural-Biology-Computing/bindflow)).
- Add bindflow support for parallel execution across multiple GPUs.


