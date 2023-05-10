We plotted the distrubitions of distances for each Zinc ion-coordinants pair of all force fields
and replicates for the simulations of the Npl4 protein consisting of the region 113-580,
containing Zinc Finger 1 (ZF1) (C137-H139-C145-C148) and Zinc Finger 2 (ZF2) (C204-H208-C216-C219).
To do so we used the compare.py script:

python compare.py -c config.yaml

The script take in input a config yaml file in wich we specify the path 
to all the distances ".xvg files" for all force fields and replicates 
computed using Gromacs tool gmx distance stored.
i.e 

md:
    ZF1:
        his139:
            charmm22*-rep1:
                replicate1/charmm22star/NH2_CT2/md/ZN_H139.xvg
            charmm36-rep1:
                replicate1/charmm36/NH2_CT2/md/ZN_H139.xvg
            charmm36-rep2:
                replicate2/charmm36/NH2_CT2/md/ZN_H139.xvg
            charmm36-rep3:
                replicate3/charmm36/NH2_CT2/md/ZN_H139.xvg
            ff99SB*-ILDN-rep1:
                replicate1/ff99SBstar-ILDN/md/ZN_H139.xvg
                ...

        cys219:
            charmm22*-rep1:
                replicate1/charmm22star/NH2_CT2/md/ZN_C219.xvg
            charmm36-rep1:
                replicate1/charmm36/NH2_CT2/md/ZN_C219.xvg
            charmm36-rep2:
                replicate2/charmm36/NH2_CT2/md/ZN_C219.xvg
            charmm36-rep3:
                replicate3/charmm36/NH2_CT2/md/ZN_C219.xvg
            ff99SB*-ILDN-rep1:
                replicate1/ff99SBstar-ILDN/md/ZN_C219.xvg


In addition, in the config file we specify the value to be plotted 
as references, one for the histidine and one for the cysteine:
I.e 

reference:
    HIS: 0.215 
    CYS: 0.238 

The reference value for the histidine was obtained by averaging 
the original distance values between the zinc ion and the histides 
in our final geometry optimization of ZF1-ZF2 systems. 
The original values were computed using GaussianView on 
systems which can be found here:

ZF1-Zn2+
../../../../../qm/npl4/6JWH/zinc_bound/zf1_CHCC_model1/dft/b3lyp/tzvp/minus1_2/reaction_mechanism/frequency/opt_frequency2_restart/zf1_zinc_opt_freq2.log

ZF2-Zn2+
../../../../../qm/npl4/6JWH/zinc_bound/zf2_CHCC_model1/dft/b3lyp/tzvp/minus1_2/reaction_mechanism/frequency/opt_frequency2_restart/zf2_zinc_opt_freq2.log
Ultimately, one can choose the final name of the plots:

out_name1: Npl4_113-580_Zn_compare_distance.pdf
