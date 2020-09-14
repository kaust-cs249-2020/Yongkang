#!/bin/bash
#SBATCH --job-name=FindClumps
#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=yongkang.long@kaust.edu.sa
#SBATCH --mail-type=END
#SBATCH --output=LOG/log.%J
#SBATCH --time=6:00:00
#SBATCH --mem=50G


#python FindClumps.py
python FindOriforThermotoga_petrophila.py
