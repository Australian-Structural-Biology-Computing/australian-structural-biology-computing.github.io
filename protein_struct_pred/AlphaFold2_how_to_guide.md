---
title: AlphaFold2 How-to Guide 
type: guide
contributors: [Michael Healey]
description: Practical guide for working with real AlphaFold data 
affiliations: [University of Queensland]
sidebar: false
toc: true
---

   
[AlphaFold2](https://www.nature.com/articles/s41586-021-03819-2) (AF2) has undoubtedly revolutionised the world of structural biology, allowing for the rapid prediction of proteins and protein complexes. In this guide I aim to equip you to understand how the algorithm works and how to interpret the output data.  
   
To do this there are 3 main sections; 

1. [AlphaFold2 - the basics](#alphafold2---the-basics-)
2. [Running a Structure Prediction](#running-a-structure-prediction), and  
3. [Interpreting the Output Files](#interpreting-the-output-files) 

This guide is designed as a supplement to [EMBLs excellent course](https://www.ebi.ac.uk/training/online/courses/alphafold/) on AF2.

## AlphaFold2 - the basics  

To start to get to grips with how AF2 goes about generating a protein model, it is helpful to understand Anfinsen’s dogma and Levinthal’s paradox.

Anfinsen’s dogma: “at least for a small globular protein in its standard physiological environment, the native structure is determined only by the protein's amino acid sequence”. This means given a random amino acid sequence it should be possible to predict the secondary structure it adopts (alpha helix, beta strand, loop etc).

![](images/AF2_How-to_images/Image-01.png)

Levinthal’s paradox: “finding the native folded state of a protein by a random search among all possible configurations can take an enormously long time.” For example, taking into account all the possible positions individual atoms can adopt in a 100 amino acid (aa) protein, there are \~3198 possible orientations.

![](images/AF2_How-to_images/Image-02.png)

It is within these two statements that we are introduced to the two problems in computational structure prediction, i) the structure prediction problem and ii) the structure folding problem. AF2 only addresses the first of these two problems and does not take into account the biophysical properties of individual atoms. 

With this in mind the next question is, how did Google DeepMind (the company behind AF2) crack the structure prediction problem? In essence they were able to do this by looking at the co-evolution of amino acid residues. We can understand this with a simple thought experiment (illustrated below). Take two amino acids in a given protein sequence, one that is positively charged (red circles), and one negatively charged (blue circles). If these two amino acids form an interacting pair together in the protein structure, then we expect this interaction to be maintained over evolutionary time. The order of the two amino acids in the sequence can be swapped, but the overall interaction between the two will remain the same. For instance, if the positively charged amino acid is mutated to become a negatively charged amino acid, then a reciprocal mutation in its partner (i.e. mutation from a negative to a positively charged amino acid) is likely to be selected during evolution to maintain the overall interaction. In other words, if amino acids interact, they are likely to co-evolve. Likewise if two residues were unrelated to each other in the structure, we would not expect to see them co-evolve (orange and green circles). By performing very deep sequence alignments it is possible to identify patterns of co-evolution between amino acids. AF2 detects these patterns to predict which amino acids are interacting, and therefore predict which amino acids are close together in 3D space. Amazingly, AF2 is able to predict protein structures with just sequence information, and has no explicit “knowledge” of how biochemistry or protein folding works. It is worth noting that while protein structures from the PDB were used as training data for AF2, this  data was only used to validate AF2’s accuracy and AF2 does not normally use protein structure data when performing a new prediction (note: there are settings you can change to adjust this). 

![](images/AF2_How-to_images/Image-03.png)

At this point it is worth stopping and taking stock of what this means for how AF2 might respond to tasks that you are interested in. Here are some questions it would be worth thinking about before moving on to the answers:

1. How would AlphaFold2 respond to the introduction of point mutations into the input sequence?  
2. How well would AlphaFold2 perform at predicting highly variable and non-conserved sequences like antibody and peptide interactions (note protein complex prediction is performed in the same manner)?

Answers:

1. Remember AF2 hasn’t solved the structure folding problem and it isn’t taking into account the physical properties of an amino acid, just its covariance across evolutionary time. As such, a single point mutation will have no appreciable effect on the overall structure of the protein prediction. The final prediction is built based on many distance restraints. You can think of this as rubber bands that hold all co-evolved residues together in such a way that the bands aren’t stretched. A single point mutation removes one restraint (one rubber band), but as the other restraints stay in place, the overall structure is unlikely to be affected.  
2. Again this comes back to the multiple sequence alignment. As the sequence of an antibody/peptide has not co-evolved with the target protein it is unlikely AF2 will be able to predict a complex. Obviously there are exceptions to this, but if you do see an accurate complex it is worth confirming if the antibody/peptide sequence has happened upon an evolutionarily conserved motif. See [this example](https://www.science.org/doi/10.1126/sciadv.abg4007) from our group where we used RaPiD to identify peptide binders which mimic a native sequence motif. 

With some of these basic concepts in mind it is time to move on to predicting a protein structure. 


## Running a structure prediction

For the purposes of this tutorial I will be using the [ColabFold](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) implementation of AlphaFold2 as it is straightforward and easy to use. This runs off the Google Colab platform which is like Google Docs but for code. Google Colab is a two tier system with a free and a paid version. The free version has access to T4 GPU cards while the paid subscription allows access to A100 GPUs. A100 GPUs are significantly better than T4 and will allow you to predict proteins faster and also increase the total number of amino acids you can input. Below is a table with some benchmarking I performed. 

| Protein (length) | VPS29 (182aa) | SNX17 (470aa) | Retriever (1442aa) |
| :---- | :---- | :---- | :---- |
| T4 (mins) | 10 | 40 | 240 |
| A100 (mins) | 3 | 7 | 30 |
| Structure | ![](images/AF2_How-to_images/29_scaled.gif) | ![](images/AF2_How-to_images/17_scaled.gif) | ![](images/AF2_How-to_images/retriever_scaled.gif) |

As residue number increases there is a big divergence in time requirements so if you are just doing a few quick runs of a short protein, T4 GPUs will work. However if you want to run lots of proteins or longer proteins I would highly recommend getting a subscription (alternatively you can register with the [Australian Alphafold Service](https://www.biocommons.org.au/alphafold#:~:text=AlphaFold%20is%20an%20artificial%20intelligence,from%20its%20amino%20acid%20sequence.), established by the Australian Biocommons and hosted  by Galaxy Australia to access a full HPC supported version. A help file on how to run an AF2 job on galaxy can be found here) . If you opt to get a subscription you need to tell Colab you would like to use an A100, to do this you can click on the arrow next to ![](images/AF2_How-to_images/change-runtime.png) and select “Change runtime type”.

Now back to how to run something on ColabFold. ColabFold works as a series of modules.

In the first module you input:

1. Your protein sequence (the easiest way to get your protein sequence is through [Uniprot](https://www.uniprot.org/)), and   
2. The name of the job. 

At this point your job is ready to run if you go to the top of the page and hit Runtime \-\> Run all you will end up with a protein structure prediction downloaded onto your computer. 

3. To predict a protein complex you simply need to add a “:” between two sequences.  
![](images/AF2_How-to_images/Image-04.png)

There are however some settings you might like to consider using:

* Num\_relax: this will use amber to do a simple relax of the protein structure, this will also significantly increase the time it takes for the prediction to occur.   
* In the second module you can set the MSA settings. Given the discussion above, you can see that this is quite an important setting. The [ColabFold paper](https://www.nature.com/articles/s41592-022-01488-1) goes into more detail about these methods. Personally I don’t adjust the default settings![](images/AF2_How-to_images/Image-05.png)
* Next there is the advanced setting list. Again, I don’t normally change these settings but I will highlight a few of the options.   
  * Model\_type: there are several different versions of the AF2 code: [the original](https://www.nature.com/articles/s41586-021-03819-2) (alphafold\_ptm) which is great for singular globular proteins but was not trained on multimeric protein structures, and 3 versions of [alphafold\_multimer](https://www.biorxiv.org/content/10.1101/2021.10.04.463034v2) this model was trained on multimeric protein complexes and each version saw improvements in prediction accuracy. Leaving this set to ‘auto’ will run the latest version of either alphafold\_ptm if you input a single protein or alphafold\_multimer if you run a protein complex.  
  * Num\_recycles: this determines how many times a structural model is fed back through the AF2 architecture and can be thought of as a refinement. In general, I find that 3 recycles is sufficient for most jobs, although if I have a poor MSA (\<200 sequences) I will tend to increase the number of recycles (in this particular case this does not always improve the outcome).

This should be enough information to allow you to run your own predictions but if you would like more information on each of the settings it can be found at the bottom of the [Colab document](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb#scrollTo=UGUBLzB3C6WN) or at the [ColabFold github](https://github.com/sokrypton/ColabFold) page. Now at this point you might be tempted to stop reading, but I encourage you not to as we are moving to the **most important** section of this How-to Guide. Which is how you interpret the outputs you will find in your download folder.


## Interpreting the output files

It is hard to overstate the importance of looking at the quality of your protein model. Just as in any other form of science, AF2 will produce a number of confidence metrics that will help you interpret if your model is good or bad. After running ColabFold you should get a downloaded .zip file. In this zip file there will be lot of files, but the 4 key files are:

1. The PDB file (this is your structure that can be opened with [Pymol](https://www.pymol.org/)/[ChimeraX](https://www.cgl.ucsf.edu/chimerax/))  
2. The sequence coverage file  
3. The Predicted alignment error plot  
4. The pLDDT plot 

Again have a think about what order you would open these files. 

If you are like me you probably really just want to get to the interesting part and look at the protein structure. But I would suggest waiting just half a minute and looking at your other outputs first. Each of these will help you interpret your structure with greater accuracy. So let's go through the outputs of a protein called *sorting nexin 17* or [SNX17](https://www.uniprot.org/uniprotkb/Q15036/entry). Firstly the sequence coverage plot.

![](images/AF2_How-to_images/Image-06.png)  
Here you can see that:

* The first \~100 aa (positions) have a really deep sequence depth (\~8000 sequences),   
* The next \~300 aa have a pretty good sequence depth (\~1000 sequences),  
* While the final \~70 aa have the lowest depth (\~500 sequences). 

Generally speaking, anything more than \~200 sequences in the alignment will give you a fairly confident model. To give context, it is worth noting that SNX17 contains 3 major structural domains. The first domain is a PX domain which is highly conserved throughout evolution. This domain starts at residue 1 and is \~100 residues in length. The second domain is known as a FERM domain and it is not seen as frequently in evolution; it starts at residue 110 and is \~300 residues in length. The final region of SNX17 is a disordered tail which is \~70 residues in length. 

The next image to look at is the pLDDT plot. pLDDT is the “predicted Local Distance Difference Test”, this is a measure of how correct AF2 thinks the placement of a residue is. It is scaled from 0-100 with 0 being unconfident and 100 being confident. 

![](images/AF2_How-to_images/Image-07.png) 

Looking at this plot we can see that AlphaFold2 is confident about the large majority of the residues in SNX17. However, there are a couple of regions in the C-terminus of the protein where it is unconfident. For illustrative purposes below I have provided an image of SNX17 coloured by pLDDT score. The arrows are colour coordinated and you can see that the dips in the pLDDT score align with the loops and disordered regions of the protein, while the folded domains are highly confident. If you compare the pLDDT plot and the sequence alignment you will also note there is a similar pattern. 

![](images/AF2_How-to_images/Image-08.png) 

The final plot to look at if we are going to understand the structure prediction is the PAE, or predicted alignment error plot. This is a measure of the confidence of the relative positioning of amino acids within a structure. The first thing to notice is that you will always have a blue line along the diagonal of these plots as each residue in the structure has 0 relative positioning error to itself and the residues immediately adjacent to it (The orange box in the figure below is a good example where this is very clear, however you can see the dark blue line running diagonally across the whole plot. This feature is present in ALL PAE plots). When residues fold into a structured domain there is less error in the relative positioning of all the residues within that domain and so you get the formation of blue squares (The greeen box in the figure below). Finally if there is an interaction between two separate structural domains or two regions of a protein, or even two separate proteins forming a complex, you will see low relative error on the diagonals corresponding to the regions that interact (The purple box in the figure below shows an example of this interaction from the large structured domain from residues 1-\~400 and a small region right at the C-terminus). In this particular case the interaction along the diagonal proved to be quite important for the function of SNX17, so if you would like to explore how these predictions can start to explain protein function you can read about that [here](https://www.nature.com/articles/s41467-024-50971-0). 

![](images/AF2_How-to_images/Image-09.png) 

To highlight the interpretation of PAE plots  further, let's also look at *DNA damage checkpoint protein 1* AF output data to see why this plot is important. If we had opened the predicted protein model and coloured it by the pLDDT score we would see an image like this:

![](images/AF2_How-to_images/Image-10.png)


You can see this model is predicted with hgih confidence to contain two structured domains (dark blue) and some low confidence disordered regions (orange). Now if we were just presented with this structure we might be tempted to think that these two domains (one which is at the N-terminus and one near  the C-terminus) are forming an intramolecular interaction as AF has packed them very close together. But one quick look at the PAE plot (Figure X) will show that there is no data suggesting that these two domains interact together . You can see we get the line down the middle as per usual and then two boxes at either end of the protein indicating the two discrete structured domains. In particular the lack of blue in the top right corner and bottom left of the PAE plots (highlighted by the green boxes) indicates that AF2 has no confidence in the relative positioning of these two domains with respect to each other. Instead the closeness of the two domains is likely an artefact of a volume minimisation function within AF used to increase computational speed, or to put it another way AF2 compresses structures into the smallest volume possible to increase computational efficiency.  The correct interpretation of this AF model is that this protein comprises two non-interacting structured domains connected by a long disordered region.

Below is a table with other proteins and their PAE plots, clicking on the protein name will redirect you to the AlphaFold database which has a great interactive PAE tool. Clicking and dragging a box around an area of the PAE plot will lead to the same area being highlighted in the structure to the left. Where possible I have also included a reference to a paper which has used AlphaFold2 to describe the protein. Note the colours are slightly different with green showing low positional error and white showing high positional error. 

| Protein | Brief description | Reference |
| :----:  | :---- | :---: |
| [SNX13](https://alphafold.ebi.ac.uk/entry/Q9Y5W8) | A four-domain protein where the N and C terminus form an intramolecular interaction. | [https://doi.org/10.3389/fcell.2022.826688](https://doi.org/10.3389/fcell.2022.826688) |
| [PDLIM1](https://alphafold.ebi.ac.uk/entry/O00151) | A protein with two domains at the N and C-terminus with a long-disordered linker. | [https://doi.org/10.1042/BST20220804](https://doi.org/10.1042/BST20220804) |
| [VPS35](https://alphafold.ebi.ac.uk/entry/Q96QK1) | Alpha-helices stacked on top of one another, this is known as a heat repeat protein |   |
| [SNX17](https://alphafold.ebi.ac.uk/entry/Q15036) | A protein with two closely associated domains and a disordered tail which makes contact with these domains. | [https://doi.org/10.1038/s41467-024-50971-0](https://doi.org/10.1038/s41467-024-50971-0) |
| [CCDC22](https://alphafold.ebi.ac.uk/entry/O60826) | This protein has a N-terminal structured domain followed by a disordered domain (although note there is some confidence in the positioning of this disorder) and a long alpha-helix. This structure of this protein becomes more rigid when incorporated into the large CCC complex. | [https://doi.org/10.1016/j.cell.2023.04.003](https://doi.org/10.1016/j.cell.2023.04.003) |
| [I7ME23](https://www.alphafold.ebi.ac.uk/entry/I7ME23) | A protein with two domains connected by a short flexible linker. | [https://doi.org/10.1038/s41467-023-37868-0](https://doi.org/10.1038/s41467-023-37868-0)
| [P51513](https://www.alphafold.ebi.ac.uk/entry/P51513) | A protein with three soluble domains connected via a long flexible linker. Two of the domains interact. | [https://doi.org/10.1016/j.str.2022.08.004](https://doi.org/10.1016/j.str.2022.08.004) |

It is also worth noting that just like any method AlphaFold2 can produce false positives. The most common of these is when a protein has a region of disorder, rather than leaving this in a disordered state AF2 likes to fold these regions into alpha-helices. A good example of this is [WAC2C](https://www.uniprot.org/uniprotkb/Q9Y4E1/entry#structure) (FAM21), which is known to have a completely disordered tail from residue 90-1341. At various points AF2 imposes some degree of secondary structure on this region, which to the best of my knowledge do not exist. This issue is significantly worse in AlphaFold3 where the disordered tail is predicted to form what looks like a domain (see below). A good way to identify false positives is to look at the pLDDT score, as you can see in this example AlphaFold3 is very unconfident about these helices. 

![](images/AF2_How-to_images/Image-11.png)

**Examining protein complexes**

Right as we come to a close there is one final exercise, which is to see how you go yourself. Below is the sequence coverage, pLDDT plot and PAE plot for a protein complex, I have also attached the structure. But before you look at the structure, look at the plots and jot down what observations you make about the structure, one thing to note is that this is a trimeric protein complex so black bars have been added to indicate where the different chains start and stop in each plot. Start by looking at the individual protein and then look in the cross boxes to see how they interact with one another.  

![](images/AF2_How-to_images/Image-12.png)

The first thing to notice is that the conservation of this sequence is consistent across the whole trimeric structure. Likewise the pLDDT score is relatively high across all three chains, with the exception of the first \~200 or so aa residues in the 3rd protein (residue 450-650 as the residue numbering is continuous). This also means we can be pretty confident about the model that AF2 has produced. In the PAE plot we can see that all three proteins are single domain proteins with the third protein (C) having a short disordered N-terminal region. If we look in the cross boxes we can see that chain A and B are not positioned relative to one another. We can however see that chain A and B are accurately positioned relative to protein C. Closer inspection shows that the front half of the N-terminal disordered region of protein C is accurately positioned with respect to chain A, and that the model is confident of chain A’s positioning toward the C-terminus of protein C. Protein B on the other hand is highly confidently positioned relative to the N-terminus of protein C but not as confident with the C-terminus. 

Alright that's a lot of words, but lets now have a look at the structure and hopefully things will become a little clearer. The data we are looking at is from a protein complex called *Retriever*, where the red protein is protein A and is called VPS29. The green protein is protein B and is called VPS26C, and the orange protein is protein C and is called VPS35L. So we can see that each protein is well ordered and structured with the exception of the N-terminus of VPS35L (orange). We can also see that while protein A and B aren’t positioned relative to each other they are positioned relative to VPS35L. We can see that VPS26C interacts with the N-terminus of VPS35L while VPS29 interacts with the C-terminus. We can also see that a region of the disordered N-terminus of VPS35L makes contact with VPS29 and the C-terminus of VPS35L. Further explanation of this complex and these interactions is available [here](https://www.cell.com/cell/pdf/S0092-8674\(23\)00398-7.pdf).  
![](images/AF2_How-to_images/Image-13.png)
