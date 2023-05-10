import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
import seaborn as sns
import os
import sys
#sns.set()
# SMALL_SIZE = 14
# MEDIUM_SIZE = 14
# BIGGER_SIZE = 16
plt.rcParams["font.family"] = 'Arial'
# plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
# plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
# plt.rc('figure', titlesize=SMALL_SIZE)  # fontsize of the figure title



if __name__ == "__main__":
    list1 = sys.argv[1]
    l= []
    df = pd.read_csv(list1)
    df_grouped1 = df.groupby(['Coordination'])
    df_grouped1.boxplot(rot=45,grid=False,fontsize='large')
    fig = plt.gcf()
    fig.set_size_inches((11,7), forward=False)
    plt.tight_layout()
    plt.savefig('Figure3B_ZF1.pdf',dpi=600)

