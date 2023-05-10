pdb='/data/raw_data/computational_data/simulations_data/card/npl4/zinc_bound/6JWH_129-151/exp/replicate1/charmm22star/NH2_CT2_terminals/ini_pdb/model_6jwh_129-151_final.pdb'

./xtc2shp $pdb $pdb -c config.yaml -o starting_pdb.shp

echo "$ coordination ZF1
! keyword, name of coords. file
%external starting_pdb.ZF1.shp
%fullout
4 1
1 2 3 4 " > 6jwh_129-151.dat

shape 6jwh_129-151.dat
