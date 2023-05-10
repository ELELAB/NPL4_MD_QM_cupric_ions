import sys
import glob
import numpy as np
import matplotlib 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14 
plt.rcParams["font.family"] = 'Arial'
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=SMALL_SIZE)  # fontsize of the figure title


if __name__ == '__main__':
    data = sys.argv[1]
    data2= sys.argv[2]
    data3= sys.argv[3]
        # read each xvg belonging to that residue and replicate
    
    with open(data) as f:
        l=[]
        for line in f:
            line = line.rstrip()
            if line.startswith("#") or line.startswith("@"):
                continue
            else:
                line = line.split()
                l.append ([float(line[0]),float(line[1])])
    df = pd.DataFrame(l)
    df.columns = ["Time (ns)", 'Distance (Å)']
    df['Time (ns)']= df['Time (ns)']*0.001 # convert in ns
    df['Distance (Å)']= df['Distance (Å)']*10 # convert in ns
    #df = df.apply(pd.to_numeric, errors='ignore')
   
    with open(data2) as f1:
        l1=[]
        for line in f1:
            line = line.rstrip()
            if line.startswith("#") or line.startswith("@"):
                continue
            else:
                line = line.split()
                l1.append ([float(line[0]),float(line[1])])
    df1 = pd.DataFrame(l1)
    df1.columns = ["Time (ns)", 'Distance (Å)']
    df1['Time (ns)']= df1['Time (ns)']*0.001 # convert in ns
    df1['Distance (Å)']= df1['Distance (Å)']*10 # convert in ns
    #df = df.apply(pd.to_numeric, errors='ignore')

    with open(data3) as f2:
        l2=[]
        for line in f2:
            line = line.rstrip()
            if line.startswith("#") or line.startswith("@"):
                continue
            else:
                line = line.split()
                l2.append ([float(line[0]),float(line[1])])
    df2 = pd.DataFrame(l2)
    df2.columns = ["Time (ns)", 'Distance (Å)']
    df2['Time (ns)']= df2['Time (ns)']*0.001 # convert in ns
    df2['Distance (Å)']= df2['Distance (Å)']*10 # convert in ns
    #df = df.apply(pd.to_numeric, errors='ignore')

    i = [df,df1,df2]
    for dataframe in i:
        plt.plot(dataframe['Time (ns)'],dataframe['Distance (Å)'])
        plt.xlabel('Time (ns)')
        plt.ylabel('Distance (Å)')
    #plt.title("")
    plt.legend(['Replicate 1', 'Replicate 2', 'Replicate 3 '],loc="best")
    plt.tight_layout()
    
    plt.savefig("figureS2.pdf",dpi=300)
