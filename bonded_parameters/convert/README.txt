The python script convert_AMBERff_AMBER-to-GROMACS.py performs the conversion of AMBER force field parameters from the AMBER software format to the GROMACS format
To run the script 

python convert_AMBERff_AMBER-to-GROMACS.py

The script will ask to paste line-by-line the correct parameters from the parm99.dat/frcmod.ff99SB/frcmod.ff99SBildn files in the AMBER force field folder of AMBER software (avoid including the comments, i.e. everything from the character “!” till the end of the line). 
The script produces separate txt files with the converted parameters that need to be included in the correct itp files i.e. ffbonded.itp and ffnonbonded.itp in the AMBER force field folder of GROMACS (simply by copy, paste, and adjusting the format).  

N.B. The script works only with the conversion of the dihedral parameters that in the AMBER force field in AMBER format have a divider number of 1. Do not use this script for converting dihedral parameters with a divider number different than 1. 

When converting a set of new parameters is also a recommended procedure to include also a set of known parameters that can be used as a reference to check that everything has been converted in a proper way. A reference set of known parameters is here included.

This set of parameters can be used as a test to check the script  convert_AMBERff_AMBER-to-GROMACS.py, just paste the parameters in the AMBER format and check that the output correspond to the GROMACS format output

 (AMBER format)
BOND
!atom type Kb          b0
C -C   310.0    1.525       Junmei et al, 1999
C -OS  450.0    1.323       Junmei et al, 1999


ANGLE
!atom types     Ktheta    Theta0   Kub     S0
C -C -O     80.0      120.00    Junmei et al, 1999 acrolein
C -C -OH    80.0      120.00    Junmei et al, 1999


DIHEDRALS
!atom types             Kchi    n   delta
HO -OH -C -O       2.30        180.0            -2.0         Junmei et al, 1999
HO -OH -C -O       1.90          0.0             1.0         Junmei et al, 1999


NON BONDED
!atom  ignored    epsilon      Rmin/2   ignored   eps,1-4       Rmin/2,1-4
P           2.1000  0.2000             JCC,7,(1986),230;


AMBER (GROMACS port)
[ bondtypes ]
;      i        j  func           b0           kb
C -C 1 0.1525 259408.0
C -OS 1 0.1323 376560.0

[ angletypes ]
;      i        j        k  func       theta0       ktheta          ub0          kub
C -C -O 1 120.0 669.44
C -C -OH 1 120.0 669.44


[ dihedraltypes ]
;      i        j        k        l  func         phi0         kphi  mult
HO -OH -C -O 9 180.0 9.6232 -2.0
HO -OH -C -O 9 0.0 7.9496 1.0

[ non bonded ]
; i rmin epsilon
P   3.74177e-01  8.36800e-01


The set of parameters that we converted in the GROMACS format are from the file zf1.dat and cf1.dat
We used the convert_AMBERff_AMBER-to-GROMACS.py to convert them and the output are included in the txt files ANGLES.txt  DIHEDRALS.txt  NONBONDED.txt BONDS.txt   IMPROPERS.txt   
Since the QM structure included a CH3 instead of the Calpha we renamed CX to CT to have the correct atom type for Calpha in AMBER ff 
The converted parameters have been included in the GROMACS port of ff99SBstar_ildn and we called it amber99sb-star-ildn_Ulf_2023_bonded_zn_cu_2plus.ff


