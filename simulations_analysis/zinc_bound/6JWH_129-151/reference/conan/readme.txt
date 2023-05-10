#We calculated the CONAN analysis on the starting structure after start step of premd of 6JWH_129-151 with Zn
#We copied here the file start.pdb from /data/raw_data/computational_data/simulations_data/card/npl4/zinc_bound/6JWH_129-151/exp/replicate1/charmm36m/NH2_CT2_terminals/pre_md/0-start 

### Requirements ###
1.index_files
2.filt_tprs
3.filt_trjs  
4.frames 
####CONAN ANALYSES####

### be connected with graphical interface (ssh -X or -Y)
### source virtual environment for python3

source /usr/local/envs/py37/bin/activate

### source gromacs
source /usr/local/gromacs-2019.4/bin/GMXRC.bash

### if it doesn't work check that you have gmx_mpi in the path with which gmx_mpi

### conan is installed in: /usr/local/conan/conan.py

#input files and scripts needed to star the analyses:
-> clean.sh  (to use at the end to clean up unwanted files) 
-> conan_analysis.sh  (to run the analyses)
-> fine.inp  (to declare location of inputs xtc, tpr and reference pdb)
-> labels_gnuplot.txt (for plotting/labeling purpousing)
-> start.pdb (for reference of aminoacid types) copy it has
-> single_heatmaps.R (to use at the end on the folder plots to collect the heatmaps of the contacts of each residue)

#at the end of the analyses a number of outputs will be created including subfolders
#files:
-> dmf.xpm
-> dm.xpm
-> domains.gnu 
-> domains_1d.gnu

#subfolders:
-> aggregate (raw data and plots of the contact maps) 
   most useful file: timeline.dat
-> frames 
-> cluster_trj
-> movies
-> input 
-> matrices

-> plots

some of the folders above can be removed after analyses (with clean.sh if available) 

#modify the fine.inp file wih the right paths

#to run use tsp

tsp -N 1 ./conan_analysis.sh >& log &

