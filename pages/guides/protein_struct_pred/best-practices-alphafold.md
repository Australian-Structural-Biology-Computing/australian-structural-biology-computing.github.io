---
title: Best practices for presenting and sharing AlphaFold models in a paper
description: Have you recently started using AlphaFold and want to include its structural predictions in your paper, but don't know the best way to do so? In this short guide, we clarify what you should include so that your work is clear and reproducible for the reader.
type: Guide
contributors: [James Lingford]
affiliations: [Monash University]
toc: true
sidebar: false
redirect_from: /website/best-practices-alphafold
---

AlphaFold structural models are appearing in papers more frequently. As such, it’s important that the scientific community agree on:

* General guidelines on how to best present AlphaFold models: AlphaFold models presented without sufficient information might mislead readers into thinking the model confidence is higher than it really is. 
* Guidelines for sharing AlphaFold output files: AlphaFold models are computationally expensive to generate, and some readers might not have the resources to re-generate the model. 

For these reasons, we have distilled our knowledge, and that of the broader field, into a guide for presenting and sharing AlphaFold models in papers. The guide is not intended to be exhaustive or dogmatically rigid, and we expect it will evolve over time. Our goals with this guide are to:

1. Help newcomers get up to speed with how-to present AlphaFold models, and 
2. Encourage wider discussion among the structural biology community. 

Please reach out to us if you have suggestions.


## What AlphaFold data should I include?

The minimum AlphaFold information that should be presented in a manuscript is the following:

* AlphaFold models should be labelled as such, either in the figure or in the figure legend, so as to avoid being confused with experimentally validated models.
* The top ranked AlphaFold model should be presented, whereas lower ranked models can be included as supplementary data.
* Include a figure (main or supplemental) showing the AlphaFold model coloured by pLDDT score, with the corresponding pLDDT colour key present in the same figure.
* Include a figure (main or supplemental) showing the PAE plot, with the corresponding PAE colour key.
* Include the pTM score and ipTM score (if applicable) in a figure or in a supplementary table.

How a protein structure is presented in a paper will depend on many considerations that will be unique to each paper. Such considerations include what information exactly you are hoping to communicate, what details are most relevant to show in a figure, space constraints, choice of colour palette, and so on. That said, it is always important to remember that **a protein structure is a model, and all models have limits to their predictive accuracy.**

For example, papers that present cryo-EM structures of a protein will often show both the cryo-EM density map of a protein (i.e. the empirical data) followed by a cartoon of the protein fit to the density map (i.e. the protein model). Sometimes the cryo-EM density map has high resolution, and a model of a protein backbone can only fit one specific way into the density. Such a situation demonstrates a high confidence protein model backed up by the empirical data of the density map. At other times the electron density might be low resolution, and a protein model can feasibly fit into the density map in a few different ways. In this situation, we would have less confidence in the protein model, and this might limit the sort of scientific claims we can confidently make. 

Just like protein models built with cryo-EM, AlphaFold comes with information about model confidence. It is crucial that this information regarding AlphaFold confidence is included somewhere in the paper. The important metrics that should be included are pLDDT scores, PAE plots, pTM scores, and ipTM scores (for protein complexes only). For a short introduction to what these metrics are and how to think about them, please see the EMBL-EBI’s guides to [pLDDT](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/), [PAE](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/), and [pTM/ipTM](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/confidence-scores-in-alphafold-multimer/).

## Best practices for presenting models

### Have a supplementary figure dedicated to your top ranked AlphaFold model

We recommend having a supplementary figure dedicated to showing your top ranked AlphaFold model in cartoon form, with the backbone coloured by pLDDT score confidence, alongside its corresponding PAE plot and pTM/ipTM scores. The colour keys for pLDDT and PAE scores should also be included in this supplemental figure. These key pieces of information are important to communicate the model confidence to the reader, which allows the reader to judge the quality of the model for themselves.

### Label AlphaFold models as models in figures

It should be made obvious to the reader when a protein model is an AlphaFold model, so as to not mislead the reader into making them believe the model was solved with X-ray crystallography or cryo-EM. This can be done by labelling the model in the figure, or stating it in the figure legend text. In addition to this explicit labelling, we believe it’s good practice to provide an image of the AlphaFold protein model coloured by pLDDT score, and include a pLDDT colour key. Most readers will implicitly recognise an AlphaFold model as soon as they see a protein cartoon coloured by pLDDT scores. This is because pLDDT scores have become synonymous with AlphaFold models.

## Other good practices

### Compare all five of Alphafold’s structure predictions

AlphaFold generates five separate predictions of a protein structure and ranks them by confidence metrics. It is useful to compare all five models against each other to demonstrate an overall consistency (or inconsistency) in the model confidence. Most AlphaFold structures will be highly similar across all five models, but sometimes the five models can have noticeably different structures. This could indicate that AlphaFold has issues predicting structures for this sort of protein, maybe as a result of insufficient MSA depth or AlphaFold not being sufficiently trained on such sequences/structures. Therefore, showing all five models superposed in a single figure can communicate the consistency or inconsistency of AlphaFold’s structural predictions. This is particularly important when modelling protein-protein interactions, consistent positioning of an interaction partner over the 5 models is a good indicator of a true interaction.

### Include a figure showing the MSA generated by AlphaFold2

Including a figure of the MSA generated by AlphaFold2 can also communicate valuable information about model confidence. MSAs that lack sufficient depth – at least ~[100 sequences](https://www.nature.com/articles/s41586-021-03819-2#Sec7) at any single amino acid site – can lead to lower confidence predictions. ColabFold is an instance of AlphaFold that can generate these MSA depth figures.

#### Examples of good AlphaFold model presentation:

* Mifsud, J.C.O., Lytras, S., Oliver, M.R. et al. Mapping glycoprotein structure reveals Flaviviridae evolutionary history. Nature (2024). [ https://doi.org/10.1038/s41586-024-07899-8 ](https://doi.org/10.1038/s41586-024-07899-8)
    * **Fig. 2**
    * **Extended Data Fig. 2**
* Podvalnaya, N., Bronkhorst, A.W., Lichtenberger, R. et al. piRNA processing by a trimeric Schlafen-domain nuclease. Nature (2023). [https://doi.org/10.1038/s41586-023-06588-2](https://doi.org/10.1038/s41586-023-06588-2)
    * **Extended Data Fig. 4**
* Madhuprakash, J., et al. A disease resistance protein triggers oligomerization of its NLR helper into a hexameric resistosome to mediate innate immunity. bioRxiv (2024). [https://doi.org/10.1101/2024.06.18.599586](https://doi.org/10.1101/2024.06.18.599586)
    * **Fig. 5 & 6**
    * **Supp. Fig. 5, 6, 8**
* Vorländer, M.K., Rothe, P., Kleifeld, J. et al. Mechanism for the initiation of spliceosome disassembly. Nature (2024). [https://doi.org/10.1038/s41586-024-07741-1](https://doi.org/10.1038/s41586-024-07741-1)
    * **Extended Data Fig. 5**
* Healy, M., McNally, K.E., Butkovič, R., Chilton, M. et al. Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome (2024) Cell. [https://doi.org/10.1016/j.cell.2023.04.003](https://doi.org/10.1016/j.cell.2023.04.003)
    * **Supp. Fig. 3**

## What should I include in the methods section?

The minimum AlphaFold methodology info that should be included in the methods section is the following:

* The specific implementation of AlphaFold used (e.g. AlphaFold2 or 3, ColabFold, LocalColabFold, OpenFold, etc.)
* All software version numbers 
* The sequence databases that were queried (not applicable for AlphaFold3). 
* The running parameters used, such as model type, templates used, number of recycles, recycle early stop tolerance, amber relax settings, seed numbers, etc. It is normally sufficient to list the parameters that you changed or explicitly specified, and note that all other parameters were kept on their defaults.
* Citations to primary literature.
* Links to relevant software that were used such as GitHub repositories, Colab notebooks, Docker containers, and web servers if applicable.

Like all scientific methodology, the methods section on how AlphaFold was used should be descriptive enough that anyone would be able to replicate your outputs. There are now a few versions of AlphaFold2, as well as “forks” of AlphaFold2 like ColabFold. To ensure reproducibility, it is important to specify exactly what version of the software was used. Likewise, if installation of the software or any dependencies are altered from the original software, it will also be necessary to describe these differences. In such a case, it is probably easier for both the readers and the authors if the authors provide a link to a GitHub repository containing their modified version of the AlphaFold software. This GitHub repository should include a README file with installation and running instructions.

{% include callout.html type="note" content="Did you know that by using digital object identifiers (DOIs), you can create a link that doesn’t break for software, including modified versions. [See this link to find out how to do this for GitHub](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)." %}

Describing the parameters used to run AlphaFold2 is very important for proper reproducibility. The AlphaFold2 software has defaults for all their running parameters, but often you will want to change these parameters. Parameters that are often changed include:

* Query database (in the case of ColabFold), 
* Model type, 
* Number of recycles, 
* Recycle early stop tolerance, and 
* If amber relax was used. 

It is good practice to describe the settings used for these common parameters in your methods anyway, even if they were kept on their default settings. It’s best to err on the side of writing more descriptive methods sections than less descriptive ones.

Lastly, the creators of any software used should be properly cited. If you are using AlphaFold2, some common articles and resources you will probably need to cite will be: 

* Jumper et al. "Highly accurate protein structure prediction with AlphaFold." Nature (2021) doi: [10.1038/s41586-021-03819-2](https://www.nature.com/articles/s41586-021-03819-2)
* If you’re using AlphaFold-multimer, please also cite: Evans et al. "Protein complex prediction with AlphaFold-Multimer." biorxiv (2021) doi: [10.1101/2021.10.04.463034v1](https://www.biorxiv.org/content/10.1101/2021.10.04.463034v2)
* If you’re running AlphaFold2 via ColabFold, please also cite: Mirdita M, Schütze K, Moriwaki Y, Heo L, Ovchinnikov S and Steinegger M. “ColabFold: Making protein folding accessible to all.” Nature Methods (2022) doi: [10.1038/s41592-022-01488-1](https://www.nature.com/articles/s41592-022-01488-1)
* If you’re running AlphaFold2 via OpenFold, please also cite: Ahdritz, G., Bouatta, N., Floristean, C. et al. OpenFold: retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization. Nat Methods (2024). doi: [10.1038/s41592-024-02272-z](https://www.nature.com/articles/s41592-024-02272-z)


## What AlphaFold data should I share?

The minimum AlphaFold data that we recommend sharing is the following:

* The input amino acid sequence(s) used. Preferably in fasta file format or in a supplementary table. If the input has multiple sequences (i.e. if it’s a multimer), the identities of individual subunits should be clear for the reader.
* If AlphaFold3 was used, the input .json file should be included. These files can include information about post-translational modifications and ligands that are difficult to communicate in other file formats.
* All five .pdb or .cif output files generated by AlphaFold’s five deep learning models, as well as their corresponding .json files for PAE information. A good repository for depositing this information is [ModelArchive](https://modelarchive.org/). 
* Any non-standard scripts that were used to run AlphaFold.
* Any structure prediction models that were trained in a new way by the authors.

In an ideal world all data should be presented and shared in a paper. However, page and space limitations often require that some data be relegated to supplementary data files that readers can download separately for themselves. Places to upload AlphaFold supplementary data files include the journal website that publishes your paper, a GitHub repository, or a [Figshare](https://figshare.com/) repository. Figshare is the best option for uploading all your data as it has large storage capabilities and is free to use for academics under 20GB data. [ModelArchive](https://modelarchive.org/) is also a good option for uploading structure files, this will generate an accession code for easy reference in your paper. The key here is the DOI, which provides on-going access to the information.

AlphaFold2 generates an .a3m file during the initial sequence query stage of running the program. These files should ideally be shared too, since they are useful for replicating AlphaFold2 outputs and for investigating MSA depth. However, these files also tend to be very large and can quickly fill up storage space. If this is a concern, .a3m files can be excluded so long as the methods are clear on how to replicate them (see methodology recommendations above). The .a3m files can also be generated without the need of a GPU, which makes it less expensive for readers to re-generate these files if they so choose.







