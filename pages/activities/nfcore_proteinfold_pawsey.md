---
title: Porting software to AMD to enable nf-core ProteinFold at Pawsey
description: Port software to AMD to allow the deployment of the nf-core ProteinFold workflow at Pawsey Supercomputing Research Centre.
type: Activity_in_progress
roadmap: A shared platform, or platforms (Roadmap D3Ab)
roadmap_category: Shared-platform
contributors: [Sarah Beecroft, Joshua Storm Caley]
toc: false
redirect_from: /website/nfcore_proteinfold_pawsey
tiles:
  - title: "Visit the software resources page to see the tools ported to AMD GPUs"
    url: /software
  - title: "See version 2.0.0 of the nf-core/proteinfold workflow"
    url: https://nf-co.re/proteinfold/2.0.0/
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
- Adapt containers for compatibility with nf-core proteinfold.
- Test nfcore proteinfold workflow at Pawsey.


### In Progress

- ProteinFold config optimized for Pawsey.


### Future

- Port software to AMD that has been prioritised by the community.


### Acknowledgements

This work was supported by Australian BioCommons and the Pawsey Supercomputing Research Centre (https://ror.org/04f2f0537). Australian BioCommons receives NCRIS funding through Bioplatforms Australia. Pawsey Supercomputing Research Centre receives funding from the Australian Government and the Government of Western Australia.
