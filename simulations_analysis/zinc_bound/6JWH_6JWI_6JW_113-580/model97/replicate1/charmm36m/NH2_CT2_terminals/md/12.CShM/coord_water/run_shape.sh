modelID=$1
replicate=$2
forcefield=$3
capping=$4
simdir="../../../../../../../../../../simulations/zinc_bound/$1/model97/$2/$3/$4/md/Mol_An_water"



# Convert vertices in the traj in the input file
./xtc2shp ${simdir}/traj_nojump_mol_ur_500dt.gro ${simdir}/traj_nojump_mol_ur_dt500_fitted.xtc -c config.yaml -o traj.shp


echo "$ coordination ZF1
! keyword, name of coords. file
%external traj.ZF1.shp
%fullout
6 1
1 2 3 4 5" > r1_6jwh_113-580_charmm36_ZF1.dat

shape r1_6jwh_113-580_charmm36_ZF1.dat

python avg_plotting.py -i r1_6jwh_113-580_charmm36_ZF1.tab -c 6 -plot -box -avg -o r1_6jwh_113-580_charmm36_ZF1 -ref 0.810

echo "$ coordination ZF2
! keyword, name of coords. file
%external traj.ZF2.shp
%fullout
6 1
1 2 3 4 5" > r1_6jwh_113-580_charmm36_ZF2.dat

shape r1_6jwh_113-580_charmm36_ZF2.dat

python avg_plotting.py -i r1_6jwh_113-580_charmm36_ZF2.tab -c 6 -plot -box -avg -o r1_6jwh_113-580_charmm36_ZF2 -ref 0.448
