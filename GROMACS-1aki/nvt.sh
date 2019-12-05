#!/bin/bash
#SBATCH --job-name=gmx_nvteq
#SBATCH --mail-type=ALL
#SBATCH --mail-user=andrewrgarcia@ufl.edu
#SBATCH --output=gmx_nvteq.out
#SBATCH --error=gmx_nvteq.err
#SBATCH --time=06:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2000
#SBATCH --account=chm6586
#SBATCH --qos=chm6586

cd $SLURM_SUBMIT_DIR
module load intel/2018 openmpi/3.1.2 gromacs

gmx mdrun -deffnm nvt
