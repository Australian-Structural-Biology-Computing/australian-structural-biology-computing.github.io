---
title: Batch Structure Prediction Workflows
description: Developing optimized batch workflows for structure prediction.
type: activity_in_progress
roadmap: A shared platform, or platforms (Roadmap D3A)
roadmap_category: D3
contributors: [Ziad Al-Bkhetan, Mitchell O'Brien, Joshua Storm Caley, Keiran Rowell, Cameron Hyde, Thomas Litfin]
toc: false
redirect_from: /website/batch_structure_prediction
---

## Details

- Structure prediction software often natively supports single predictions.
- Specific workflows can re-use MSA input to massively improve efficiency over naive implementation.
    - Interaction screening where 1 protein is predicted in combination with many others.
    - Conformation sampling where 1 system is predicted with downsampled MSA with many random seeds.
    - Epitope mapping where 1 antibody-antigen system is predicted with many seeds to identify candidate binding epitope.
    - Stoichiometry screen where 1 system is predicted with many candidate stoichiometries.

This activity involves developing optimized batch workflows for structure prediction.

### Completed

- Add support for re-using MSAs to Galaxy Australia AlphaFold2 service.

### In Progress

- Add local implementation of batch colabfoldsearch to the nfcore **[proteinfold](https://nf-co.re/proteinfold/1.1.1)** pipeline.
- Add mmseqs-GPU support to the nfcore **[proteinfold](https://nf-co.re/proteinfold/1.1.1)** pipeline.
- Add boltz interaction screening workflow to screen multiple potential partners against a protein (re-using MSA for anchor protein).
- Add option for extreme replicate sampling for AlphaFold2.

### Future

- Develop Galaxy workflow to take advantage of re-using MSAs.
- Add stoichiometry screening workflow to the nfcore **[proteinfold](https://nf-co.re/proteinfold/1.1.1)** pipeline.