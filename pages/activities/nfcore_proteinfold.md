---
title: nf-core ProteinFold v2.0 Release
type: activity_inprogress
---

### Details:

- Molecular structure prediction tools require large reference databases and varied computational infrastructure
- Nextflow provides the tools to standardize workflows for portable and optimized deployment
- nfcore ProteinFold is a nextflow pipeline with support for numerous structure prediction tools under a unified API
- The v2.0 release contributes significant new functionality to the pipeline
- Collaboration with Barcelona CRG

### Completed

- [x] Config optimized for efficient utilization for Gadi at NCI
- [x] Add RosettaFold-All-Atom
- [x] Add HelixFold3
- [x] Add Boltz-1
- [x] Add AlphaFold3 (BYO weights)
- [x] Add support for local MSA search for Boltz-1
- [x] Add standardized reporting with visualisation
- [x] Add support for quality metrics in output reporting
- [x] Add process labels to improve efficient use of infrastructure

### In Progress

- [ ] Add minituare reference databases for fast troubleshooting
- [ ] De-duplicate reference datasets across different methods

### Contributors:

- Ziad Al-Bkhetan
- Mitchell O'brien
- Joshua Cayley
- Keiran Rowell
- Thomas Litfin