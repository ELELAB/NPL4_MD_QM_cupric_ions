#!/usr/bin/python

# convert_AMBERff_AMBER-to-GROMACS.py - convert AMBER force field parameters from AMBER software format to GROMACS format
#
#     Copyright (C) 2023
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import math

print("prog started")

print("inserting BONDS lines (insert null line to exit insertion)")
fileB = open("BONDS.txt","w")
while 1:
    touple = raw_input()
    ts = str(touple).rsplit()
    if touple != "":
        sig,sig2,kb,b0 = ts
        # tansform + write file part
        t1 = str(sig)+ " " + str(sig2)+ " "  + "1" + " " + str(float(b0)/float(10))+ " "  + str(float(kb)*float(4.184)*float(1000)*(float(2)/float(10))) + "\n"
        fileB.write(t1)
    else:
        break
fileB.close()

print("inserting ANGLES lines (insert null line to exit insertion)")
fileA = open("ANGLES.txt","w")
while 1:
    touple = raw_input()
    ts = str(touple).rsplit()
    if touple != "":
        sig,sig2,sig3,ktheta,theta0 = ts
        # tansform + write file part
        t1 = str(sig)+ " "  + str(sig2)+ " "  + str(sig3)+ " "  + "1"+ " "  + str(float(theta0))+ " "  + str(float(ktheta)*float(4.184)*float(2))+ "\n"
        fileA.write(t1)
    else:
        break
fileA.close()

print("inserting DIHEDRALS lines (insert null line to exit insertion)")
fileD = open("DIHEDRALS.txt","w")
while 1:
    touple = raw_input()
    ts = str(touple).rsplit()
    if touple != "":
        sig,sig2,sig3,sig4,kcmi,delta,h = ts
        # tansform + write file part
        t1 = str(sig)+ " "  + str(sig2)+ " "  + str(sig3)+ " " +str(sig4)+ " " + "9"+ " "  + str(float(delta))+ " "  + str(float(kcmi)*float(4.184))+ " " +str(abs(float(h)))+ "\n"
        fileD.write(t1)
    else:
        break
fileD.close()

print("inserting IMPROPERS lines (insert null line to exit insertion)")
fileI = open("IMPROPERS.txt","w")
while 1:
    touple = raw_input()
    ts = str(touple).rsplit()
    if touple != "":
        sig,sig2,sig3,sig4,kpsi,psi0 = ts
        # tansform + write file part
        t1 = str(sig)+ " "  + str(sig2)+ " "  + str(sig3)+ " " +str(sig4)+ " " + "2"+ " "  + str(float(psi0))+ " "  + str(float(kpsi)*float(4.184)*float(2))+ "\n"
        fileI.write(t1)
    else:
        break
fileI.close()

print("inserting NONBONDED lines (insert null line to exit insertion)")
fileNB = open("NONBONDED.txt","w")
while 1:
    touple = raw_input()
    ts = str(touple).rsplit()
    if touple != "":
        sig,rmin2,epsilon = ts
        # tansform + write file part
        t1 = str(sig)+ " " + str((float(rmin2)/float(10))*(float(2)/float(pow(float(2),float(1)/float(6)))))+ " "  + str(abs(float(epsilon)*float(4.184)))+ "\n"
        fileNB.write(t1)
    else:
        break
fileNB.close()

