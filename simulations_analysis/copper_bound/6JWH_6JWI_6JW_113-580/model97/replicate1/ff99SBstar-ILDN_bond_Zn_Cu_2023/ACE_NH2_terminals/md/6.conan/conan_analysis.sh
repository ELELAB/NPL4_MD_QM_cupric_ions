#!/usr/bin/env bash 
#executes CONAN analysis
# declare the group of atoms for the analysis -> 1. Protein

source /usr/local/gromacs-2022.3/bin/GMXRC.bash

cp ../4.frames/pdbmovie_1.pdb reference.pdb
/usr/local/conan/conan.py fine.inp << eof 
0
eof 


