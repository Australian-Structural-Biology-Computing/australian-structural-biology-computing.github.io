---
title: OpenOnDemand GUI ProteinFold app
description: An Open OnDemand application providing a graphical interface to nf-core/proteinfold on HPC systems.
type: Completed_activity
roadmap: A shared platform, or platforms (Roadmap D3Ac)
roadmap_category: Shared-platform
contributors: [Matthew Downton, Kisaru Liyanage, Wenjing Xue, Joshua Storm Caley, Keiran Rowell, Thomas Litfin]
toc: false
redirect_from: /website/nci_ood_proteinfold
tiles:
  - title: View the Open OnDemand ProteinFold application
    url: https://github.com/Australian-Structural-Biology-Computing/ood-proteinfold
---

{% include tiles-simple.html target="tiles" col="1" variant="simple" %}

## Details

- Numerous structure prediction methods are available via the command line.
- Web services with graphical interfaces are freely available with limited capacity.
- Open OnDemand provides a simple graphical interface to HPC systems.
- Several institutional HPCs have an OpenOnDemand deployment (e.g. KOD @ UNSW, ARE @ NCI).

### Completed

- Developed and hosted the pilot application on Katana at UNSW.
- Published the application for adaptation to other Open OnDemand deployments.
- Added researcher-friendly sequence, FASTA, and samplesheet inputs.
- Added support for multiple nf-core/proteinfold prediction methods and configurable run parameters.
- Made results and run diagnostics accessible through the web interface.

{% include callout.html type="note" content="An NCI deployment of this Open OnDemand application is not currently planned. The published application remains available for other institutions to adapt to their HPC environment." %}

<figure>
<img src= "images/activities/ood-proteinfold.png" alt="KOD-proteinfold" style="border: 4px solid black; width: 50%; height: 50%">
<figcaption> Screenshot from the Katana OnDemand ProteinFold app deployed at UNSW.</figcaption>
</figure>
