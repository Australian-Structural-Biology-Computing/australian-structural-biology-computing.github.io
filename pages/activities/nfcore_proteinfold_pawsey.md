---
title: Porting software to AMD to enable nfcore/proteinfold at Pawsey
description: Ported software to AMD to enable deployment of the nfcore/proteinfold workflow at Pawsey Supercomputing Research Centre.
type: Completed_activity
roadmap: A shared platform, or platforms (Roadmap D3Ab)
roadmap_category: Shared-platform
contributors: [Sarah Beecroft, Joshua Storm Caley]
toc: false
redirect_from: /website/nfcore_proteinfold_pawsey
tiles:
  - title: "Visit the AMD porting page to see the tools available for AMD GPUs"
    url: /amd_porting
  - title: "See version 2.0.0 of the nf-core/proteinfold workflow"
    url: https://nf-co.re/proteinfold/2.0.0/
  - title: "Use the nf-core Pawsey Setonix profile"
    url: https://nf-co.re/configs/pawsey_setonix/
  - title: "Read the Pawsey user documentation"
    url: https://pawsey.atlassian.net/wiki/spaces/US/pages/1881735179/Using+NF-core+Proteinfold+on+Setonix
---


{% include tiles-simple.html target="tiles" col="2" variant="simple" %}


## Details

- Deep Learning models work natively with NVIDIA hardware.
- Setonix at Pawsey contains a large number of AMD GPUs.
- Models can be made to work with AMD hardware available at Pawsey.


### Completed

- Build AMD compatible container for AlphaFold2.
- Build AMD compatible container for ColabFold.
- Build AMD compatible container for Boltz-1.
- Build AMD compatible container for ESMFold.
- Build AMD compatible container for Boltz-2.
- Adapt containers for compatibility with nf-core/proteinfold.
- Test nfcore/proteinfold workflow at Pawsey.
- Contribute a ProteinFold-specific configuration to the nf-core Pawsey Setonix institutional profile.


### Acknowledgements

This work was supported by Australian BioCommons and the [Pawsey Supercomputing Research Centre](https://ror.org/04f2f0537). Australian BioCommons receives NCRIS funding through Bioplatforms Australia. Pawsey Supercomputing Research Centre receives funding from the Australian Government and the Government of Western Australia.
