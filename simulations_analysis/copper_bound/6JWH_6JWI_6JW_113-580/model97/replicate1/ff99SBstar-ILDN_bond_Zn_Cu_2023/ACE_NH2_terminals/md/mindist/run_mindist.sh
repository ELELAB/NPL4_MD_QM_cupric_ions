#!/usr/bin/bash

modelID=$1
replicate=$2
forcefield=$3
capping=$4
simdir="../../../../../../../../../../simulations/copper_bound/$1/model97/$2/$3/$4/md/Mol_An_water"



gmx_mpi make_ndx -f ${simdir}/traj_nojump_mol_ur_500dt.gro -n index.ndx<< eof
splitres 13
eof


gmx_mpi mindist -f ${simdir}/traj_nojump_mol_ur_dt500_fitted.xtc -n index.ndx -od mindist_ZF1.xvg << eof
18
15
eof 

gmx_mpi mindist -f ${simdir}/traj_nojump_mol_ur_dt500_fitted.xtc -n index.ndx -od mindist_ZF2.xvg << eof
19
15
eof 


# Convert vertices in the traj in the input file
python mindist_count.py

