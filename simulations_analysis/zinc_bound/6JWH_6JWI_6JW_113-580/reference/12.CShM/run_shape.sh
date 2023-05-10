pdb="/data/raw_data/computational_data/simulations_data/card/npl4/zinc_bound/6JWH_6JWI_6JW_113-580/model97/replicate1/charmm36m/NH2_CT2_terminals/ini_pdb/npl4_yeast.B99990097_charmm36.pdb"



# Convert vertices in the traj in the input file
./xtc2shp $pdb $pdb -c config.yaml -o traj.shp


echo "$ coordination ZF1
! keyword, name of coords. file
%external traj.ZF1.shp
%fullout
4 1
1 2 3 4 " > 6jwh_113-580_charmm36_ZF1.dat

shape 6jwh_113-580_charmm36_ZF1.dat

echo "$ coordination ZF2
! keyword, name of coords. file
%external traj.ZF2.shp
%fullout
4 1
1 2 3 4 " > 6jwh_113-580_charmm36_ZF2.dat

shape 6jwh_113-580_charmm36_ZF2.dat

