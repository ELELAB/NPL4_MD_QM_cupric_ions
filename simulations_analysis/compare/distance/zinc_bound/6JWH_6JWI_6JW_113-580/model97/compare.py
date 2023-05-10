#!/usr/bin/env python

# Copyright (C) 2022, Simone Scrima

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import os.path as path
import argparse
import shutil
from pathlib import Path
import glob
import numpy as np
import logging
import pandas as pd 
import requests
import tempfile
import yaml
import re
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
plt.rcParams["font.family"] = 'Arial'
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=6)    # legend fontsize
plt.rc('figure', titlesize=SMALL_SIZE)  # fontsize of the figure title




def plot_md(d,
            ref1,
            ref2,
            out_name):

    # Prepare figure        
    fig, axs = plt.subplots(4,2, dpi=300)
    fig.set_size_inches(7, 9.1, forward=True)
    

    # Plot each ZF and residue 
    ###########
    # ZF 1
    ###########
    for (columnName, columnData) in d['ZF1']['his139'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[0][0])
    l1 = axs[0][0].axvline(ref1,
                       color='grey',
                       ls='--',
                       alpha=0.5)
    l1.set_label('QM HIS')

    fig.tight_layout()
    axs[0][0].legend(loc="best")

    for (columnName, columnData) in d['ZF1']['cys137'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[1][0])
    l2 = axs[1][0].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    fig.tight_layout()
    axs[1][0].legend(loc="best")

    for (columnName, columnData) in d['ZF1']['cys145'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[2][0])

    l2 = axs[2][0].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    fig.tight_layout()
    axs[2][0].legend(loc="best")

    for (columnName, columnData) in d['ZF1']['cys148'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,ax=axs[3][0])
    fig.tight_layout()

    l2 = axs[3][0].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    axs[3][0].legend(loc="best")

    axs[0, 0].set_title('ZF1-His139',
                         fontweight="bold")
    axs[1, 0].set_title('ZF1-Cys137',
                         fontweight="bold")
    axs[2, 0].set_title('ZF1-Cys145',
                         fontweight="bold")
    axs[3, 0].set_title('ZF1-Cys148',
                         fontweight="bold")
    axs[0, 0].set_xlabel('')
    axs[1, 0].set_xlabel('')
    axs[2, 0].set_xlabel('')
    axs[3, 0].set_xlabel('Distance ($Å$)')

    # Plot each ZF and residue 
    ###########
    # ZF 2
    ###########
    for (columnName, columnData) in d['ZF2']['his208'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[0][1])
    l1 = axs[0][1].axvline(ref1,
                       color='grey',
                       ls='--',
                       alpha=0.5)
    l1.set_label('QM HIS')
    fig.tight_layout()
    axs[0][1].legend(loc="best")

    for (columnName, columnData) in d['ZF2']['cys204'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[1][1])
    l2 = axs[1][1].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    fig.tight_layout()
    axs[1][1].legend(loc="best")

    for (columnName, columnData) in d['ZF2']['cys216'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,
                     ax=axs[2][1])
    l2 = axs[2][1].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    fig.tight_layout()
    axs[2][1].legend(loc="best")

    for (columnName, columnData) in d['ZF2']['cys219'].iteritems():
        sns.distplot(columnData,
                     hist=False,
                     label=columnName,ax=axs[3][1])
    fig.tight_layout()

    l2 = axs[3][1].axvline(ref2,
                       color='black',
                       ls='--',
                       alpha=0.7)
    l2.set_label('QM CYS')
    axs[3][1].legend(loc="best")

    axs[0, 1].set_title('ZF2-His208',
                        fontweight="bold")
    axs[1, 1].set_title('ZF2-Cys204',
                        fontweight="bold")
    axs[2, 1].set_title('ZF2-Cys216',
                        fontweight="bold")
    axs[3, 1].set_title('ZF2-Cys219',
                         fontweight="bold")
    axs[0, 1].set_xlabel('')
    axs[1, 1].set_xlabel('')
    axs[2, 1].set_xlabel('')
    axs[0, 1].set_ylabel('')
    axs[1, 1].set_ylabel('')
    axs[2, 1].set_ylabel('')
    axs[3, 1].set_ylabel('')
    axs[3, 1].set_xlabel('Distance ($Å$)')
    
    fig.tight_layout()
    plt.savefig(out_name,dpi=300)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-c',
                    '--config',
                    dest='conf',
                    type=str,
                    required=True,
                    metavar='',
                    help='config yaml'
                    )
                

    args = parser.parse_args()

    # Define Flags
    config = os.path.abspath(args.conf)
    
    # load config file
    with open(config) as c:
            parsed_yaml = yaml.load(c, 
                                    Loader=yaml.FullLoader)
    
    # Build dictionaries of dataframes replicates 298K :
    # i.e
    # d = {ZF1: {charmm22 {his139:df,cys137:df,xxxx},
    #      ...
    #            ff99SB {his139:df,cys137:df,xxxx}}}
    
    d = {}
    for zinc_finger in parsed_yaml['md']:
        zf= {}
        for position in parsed_yaml['md'][zinc_finger]:
            df_store = []
            for replicate in parsed_yaml['md'][zinc_finger][position]:
                data = parsed_yaml['md'][zinc_finger][position][replicate]
                # read each xvg belonging to that residue and replicate
                df = pd.read_csv(data,
                                skiprows=17,
                                header=None,
                                sep="   ")
                df.columns = ["Time (ps)", replicate]
                df.columns = ["Time (ns)", replicate]
                df['Time (ns)']= df['Time (ns)']*0.001 # convert in ns
                df[replicate]= df[replicate]*10 # convert in A                
                df_store.append(df.drop("Time (ns)",axis=1))
            df = pd.concat(df_store,axis=1) # merge the stored dataframe
            #df = df.loc[:,~df.columns.duplicated()] # remove duplicate columns
            zf[position] = df
        d[zinc_finger] = zf

    ref1=parsed_yaml['reference']['HIS']
    ref2=parsed_yaml['reference']['CYS']
    out1=parsed_yaml['out_name1']

    plot_md(d,ref1,ref2,out1)
