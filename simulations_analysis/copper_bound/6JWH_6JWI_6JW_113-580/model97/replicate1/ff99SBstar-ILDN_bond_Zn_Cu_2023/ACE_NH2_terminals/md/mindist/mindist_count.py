#!/usr/bin/env python


# Copyright (C) 2019, Simone Scrima <simonescrima@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

# Import libraries
import pandas as pd

# Import all data from .xvgs
df_zn1 = pd.read_csv("mindist_ZF1.xvg",
                      skiprows=24,
                      header=None,
                      sep="  ")

df_zn2 = pd.read_csv("mindist_ZF2.xvg",
                      skiprows=24,
                      header=None,
                      sep="  ")

d= { "ZF1": df_zn1, "ZF2":df_zn2 }


# Minimun and Maximum for the dfs
for zf in d:
    maximum = d[zf][1].max()
    minimum = d[zf][1].min()
    print("Maximum for " + zf , maximum)
    print("Minimum for " + zf , minimum)

# Count percentage of frame where the distance is less than 0.35
for zf in d:
    percentage = d[zf][1]<=0.35
    percentage = percentage.value_counts(normalize=True).mul(100)
    print("Percentage of frame in which the distance is less than 0.35 " + zf +"\n",percentage)
   

