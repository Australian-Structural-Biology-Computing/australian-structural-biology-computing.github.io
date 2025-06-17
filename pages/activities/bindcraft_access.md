---
title: Community Access to BindCraft
type: activity_inprogress
---

### Details

<figure>
<img src= "images/activities/bindcraft-pipeline.png" alt="BindCraft pipeline" style="width: 75%; height: 75%">
</figure>


- [BindCraft](https://github.com/martinpacesa/BindCraft) is an end-to-end solution for protein binder design.
- BindCraft was widely used by participants in a recent blind evaluation ([Adaptyv Bio](https://www.adaptyvbio.com/blog/po104)) of protein binder design tools. 
- Several independent groups generated de novo designed binders with competitive affinity to the natural ligand using the BindCraft tool.
- BindCraft tool is available within a NextFlow [workflow](https://github.com/Australian-Structural-Biology-Computing/bindflow) to support portable deployment.

:warning: Native BindCraft tool requires PyRosetta as a filter with non-commercial license

### Completed:

- [x] Wrap the BindCraft tool in a Nextflow workflow ([bindflow](https://github.com/Australian-Structural-Biology-Computing/bindflow)).
- [x] Add support for parallel execution across multiple GPUs.
- [x] Negotiate PyRosetta license for non-commercial use at NCI.
- [x] Output partial results when HPC scheduler jobs time out.

### In Progress:

- [ ] Install workflow at NCI.
- [ ] Release BindCraft fork without PyRosetta dependancy.
- [ ] Release BindCraft fork with open-source replacements for PyRosetta filters.

### Future:

- [ ] OpenOnDemand app for running BindCraft from a graphical web interface.

### Contributors:

- Ziad Al-Bkhetan
- Thomas Litfin