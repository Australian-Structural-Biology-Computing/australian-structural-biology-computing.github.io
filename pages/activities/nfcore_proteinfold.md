---
title: nf-core ProteinFold v2.0 Release
description: Contribute towards, and locally deploy, v2.0 of nf-core ProteinFold workflow.
type: Activity_in_progress
roadmap: A shared platform, or platforms (Roadmap D3A)
roadmap_category: Shared-platform
contributors: [Ziad Al-Bkhetan, Mitchell O'Brien, Joshua Storm Caley, Keiran Rowell, Thomas Litfin]
toc: false
redirect_from: /website/nfcore_proteinfold
---

## Details

- Molecular structure prediction tools require large reference databases and varied computational infrastructure.
- Nextflow provides the tools to standardize workflows for portable and optimized deployment.
- nfcore [ProteinFold](https://nf-co.re/proteinfold/1.1.1) is a nextflow pipeline with support for numerous structure prediction tools under a unified API.
- The upcoming v2.0 release contributes significant new functionality to the pipeline.
- [Collaboration](https://www.biocommons.org.au/news/nf-core-hackathon-2025) with Barcelona Centre for Genomic Regulation ([CRG](https://www.crg.eu/)).

### Completed

- Config optimized for efficient utilization for Gadi at NCI.
- Add new tools to the ProteinFold pipeline:
    - RosettaFold-All-Atom.
    - HelixFold3.
    - Boltz-1.
    - Boltz-2.
    - AlphaFold3 (BYO weights).
- Add support for local MSA search for Boltz.
- Add standardized reporting with visualisation.
- Add standard QC metrics to HTML report (PAE, MSA coverage).
- Add process labels to improve efficient use of infrastructure.
- De-duplicate reference datasets across different methods.
- Add miniature reference databases for fast troubleshooting.
- Update documentation and metro-map.
- Test for release.

### In Progress

- Review workflow outputs for all modes.