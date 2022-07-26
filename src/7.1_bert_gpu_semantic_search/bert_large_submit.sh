#!/bin/bash
#####  Constructed by HPC everywhere #####
#SBATCH --mail-user=abbajpai@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0-32:59:00
#SBATCH --mail-type=FAIL,BEGIN,END
#SBATCH --job-name=my_job
#SBATCH -p gpu
#SBATCH --output=out_%j.txt
#SBATCH --error=error_%j.err

######  Module commands #####
module load python/3.9.8

######  Job commands go below this line #####
python3 bert_large_model.py
