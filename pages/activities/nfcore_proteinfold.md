---
title: nf-core ProteinFold v2.0 Release
type: activity_in_progress
contributors: [Ziad Al-Bkhetan, Mitchell O'Brien, Joshua Storm Caley, Keiran Rowell, Thomas Litfin]
toc: false
---

## Details

- Molecular structure prediction tools require large reference databases and varied computational infrastructure.
- Nextflow provides the tools to standardize workflows for portable and optimized deployment.
- nfcore [ProteinFold](https://nf-co.re/proteinfold/1.1.1) is a nextflow pipeline with support for numerous structure prediction tools under a unified API.
- The upcoming v2.0 release contributes significant new functionality to the pipeline.
- [Collaboration](https://www.biocommons.org.au/news/nf-core-hackathon-2025) with Barcelona Centre for Genomic Regulation ([CRG](https://www.crg.eu/)).

### Completed

- Config optimized for efficient utilization for Gadi at NCI.
- Add RosettaFold-All-Atom.
- Add HelixFold3.
- Add Boltz-1.
- Add AlphaFold3 (BYO weights).
- Add support for local MSA search for Boltz-1.
- Add standardized reporting with visualisation.
- Add support for quality metrics in output reporting.
- Add process labels to improve efficient use of infrastructure.

### In Progress

- Add minituare reference databases for fast troubleshooting.
- De-duplicate reference datasets across different methods.