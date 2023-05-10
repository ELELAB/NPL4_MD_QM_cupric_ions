modelID=$1
replicate=$2
forcefield=$3
capping=$4
simdir="../../../../../../../../../../simulations/zinc_bound/$1/exp/$2/$3/$4/md/Mol_An_water"



# Convert vertices in the traj in the input file
./xtc2shp ${simdir}/traj_nojump_mol_ur_1000dt.gro ${simdir}/traj_nojump_mol_ur_dt1000_fitted.xtc -c config.yaml -o traj.shp


echo "$ coordination ZF1
! keyword, name of coords. file
%external traj.ZF1.shp
%fullout
4 1
1 2 3 4" > r2_6jwh_129-151_charmm36.dat

shape r2_6jwh_129-151_charmm36.dat

python avg_plotting.py -i r2_6jwh_129-151_charmm36.tab -c 4 -plot -box -avg -o r2_6jwh_129-151_charmm36 -ref 0.810
