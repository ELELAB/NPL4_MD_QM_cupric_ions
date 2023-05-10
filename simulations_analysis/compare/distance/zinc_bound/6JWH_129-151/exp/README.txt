We plotted the distrubitions of distances for each Zinc ion-coordinants pair of all force fields
and replicates for the simulations, both at 298K and at high temperature (400-500K), of the Npl4 protein 
consisting of the region 129-151, containing Zinc Finger 1 (ZF1) (C137-H139-C145-C148)
To do so we used the compare.py script:

python figure2.py -c config.yaml
python figureS1.py -c config.yaml

The script take in input a config yaml file in wich we specify the path 
to all the distances ".xvg files" for all force fields and replicates 
computed using Gromacs tool gmx distance stored.
i.e 

md:
    ZF1:
        charmm22:
            his139:
                rep1:
                    replicate1/charmm22star/NH2_CT2/md/ZN2_H139.xvg
                rep2:
                    replicate2/charmm22star/NH2_CT2/md/ZN2_H139.xvg
                rep3:
                    replicate3/charmm22star/NH2_CT2/md/ZN2_H139.xvg
                NH2-CT3:
                    replicate1/charmm22star/NH2_CT3/md/ZN2_H139.xvg
                ...

	    cys148:
		charmm22-500K:
		    replicate1/charmm22star/NH2_CT2/md_500/ZN2_C148.xvg
		ff99SB-ILDN-400K:
		    replicate1/ff99SB-ILDN/ACE_NH2_terminals/md_400/ZN2_C148.xvg
		ff99SBstar-ILDN-400K:
		    replicate1/ff99SBstar-ILDN/ACE_NH2_terminals/md_400/ZN2_C148.xvg
		ff99SB-ILDN-500K:
		    replicate1/ff99SB-ILDN/ACE_NH2_terminals/md_500/ZN2_C148.xvg
		ff99SBstar-ILDN-500K:
		    replicate1/ff99SBstar-ILDN/ACE_NH2_terminals/md_500/ZN2_C148.xvg


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

out_name1: Npl4_129-151_Zn_compare_distance_298K.pdf
out_name2: Npl4_129-151_Zn_compare_distance_400_500K.pdf

