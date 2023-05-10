Analysis of the coordination geometry by Shape software
( Alvarez et all https://doi.org/10.1016/j.ccr.2005.03.031 ).
It calculates the continuous shape measures (CShM) from a reference
polyhedra respect a geometry of interest.

-------------
Input files
-------------

The software Shape employs two input files for its calculations:
A) *.dat
B) *.shp



A) 
User generated file. It is the main input file of the software. It may contain
the following fields (fields 1-3 are optional, while field 6 can be omitted if
a keyword for reading an external coordinates file is used).


Field : 
1) Title line (up to 80 characters) indicated by the ‘$’ symbol in the first column.
2) Optional comment lines, recognized by the "!" symbol in the first column.
3) Keywords (one line for each keyword)
4) Size of the geometry of interest that we want to confront to the reference:
    - Number of vertices
    - Position of the central atom in the coordinates list (0 if there is no central atom)
5) Codes of the reference polyhedra chosen. 
6) One data set for each structure to be analyzed that comprises:
   - A label for the structure with up to 15 characters 
   - One line per atom containing a label with up to 4 characters
     and cartesian coordinates.

In our case of study it is in the following format: 

"""
$ tetrahedral Cu
! keyword, name of coords. file
%external   opt_freq_zf2_Cu
%fullout
4 1
1 2 3 4
"""

Here, we specified that:
I) our external file is called "opt_freq_zf2_Cu" (%external)
II) we want an .out file (%fullout) (described below)
III) our geometry is constituted by 4 atoms (vertices) and that we have one central 
   atom which is in the first position of the external file.
IV) we are confronting our geometry against polyhedra which have 4 vertices
   i.e

     SP-4            1 D4h   Square
     T-4             2 Td    Tetrahedron
     SS-4            3 C2v   Seesaw
     vTBPY-4         4 C3v   Vacant trigonal bipyramid


B) Is a user-generated coordinates file, specified with the "%external"
keyword in the input *.dat file (shown above). In our case it is in the 
following format:

"""
0
  Cu  17.279  48.988  66.337
  S   16.486  46.798  66.082
  S   17.450  48.779  68.679
  S   18.584  49.383  64.443
  N   16.251  50.851  66.201
"""

Here are stored the coordinates of the atoms constituting our 
geometry of interest. 

In our case we have a geometry in which the copper ion (Cu) is at the 
center (hence the first position, as specified in the field 4) 
of the .dat file. While the sulfur and nitrogen atoms constitutes the vertices of the geometry. 

To build this file we used the coordinates of the atoms from the .log output file of Gaussian stored here :
../../../../../../../../../../../../../qm/npl4/6JWH/copper_bound/zf2_CHCC_model1/dft/b3lyp/tzvp/minus1_2/reaction_mechanism/frequency/opt_frequency2_restart/zf2_cupric_opt_freq2.log 

We used the GaussianView software to extract the coordinates.

-------------
Output
-------------

The output files of the software are:

C) .out file
D) .tab

C)

Verbose file specified by using the %fullout keyword. It contains the coordinates of the
structures, the closest reference polyhedra, the CShM score and the optimal vertex pairing.

D) 

Summary of the output present in C) which shows mainly the CShM score of the geometry
with respect to the reference polyheadra. 
i.e


Structure [ML4 ]         SP-4          T-4         SS-4      vTBPY-4
 0              ,      14.463,       5.699,       3.902,       7.392



-------------
Analysis
-------------
To perform the Shape analysis just run the script with:
bash do.sh


