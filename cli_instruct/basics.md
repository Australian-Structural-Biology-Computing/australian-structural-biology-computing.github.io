---
title: CLI guide 
type: cli-guide 
contributors: [Keiran Rowell, James Lingford]
description: A blank command line guide   
affiliations: [Structural Biology Facility UNSW, Monash University]
---

Learning the command line is useful if you want to do things at scale or use anything outside of pre-built tools 


Code syntax highlighting works built-in (e.g. snippet to run AlphaFold)

```
bash
python3 docker/run_docker.py \
  --fasta_paths=your_protein.fasta \
  --max_template_date=2022-01-01 \
  --data_dir=$DOWNLOAD_DIR \
  --output_dir=/home/user/absolute_path_to_the_output_dir
```


Here's generating and RSA-key (pilfered from [jameslingford.com](jameslingford.com)) 
Among his many excellent tutorials are his guide to [running ColabFold on your uni's local cluster using SSH](https://www.jameslingford.com/blog/colabfold-hpc-ssh-howto/). 

```
bash
ssh-keygen -b 4096 -t rsa -C "Add your own personal comment between quotes"
```

