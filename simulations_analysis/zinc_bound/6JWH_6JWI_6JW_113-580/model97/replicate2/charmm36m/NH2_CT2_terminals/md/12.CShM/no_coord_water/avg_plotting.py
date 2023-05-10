import matplotlib
#matplotlib.use("Agg")
from matplotlib import pyplot as plt
import numpy as np
from collections import defaultdict
import argparse 
import pandas as pd
np.set_printoptions(suppress=True)
import seaborn as sns

def parse_tab(fname):
    # convert *.tab output from Shape
    # into dataframe
    data = []
    with open(fname) as fh:
        for line in fh:
            if line.startswith("Structure"):
                break
        for line in fh:
            tmp = line.strip().split(",")
            data.append([ float(t.strip()) for t in tmp[1:] ])
        df = pd.DataFrame(data) 
    return(df)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', 
                        dest='tab',
                        type=str,
                        help="Input file")
    parser.add_argument('-avg', 
                        dest='avg',
                        action='store_true',
                        help="output averages")
    parser.add_argument('-c', 
                        dest='coord',
                        type=int,
                        help="Coordination number",
                        default=4) 
    parser.add_argument('-box', 
                        dest='box',
                        action='store_true',
                        help="Boxplot")
    parser.add_argument('-plot',  
                        dest='plot',
                        action='store_true', 
                        help="plot")     
    parser.add_argument('-ref',  
                        dest='ref',
                        type=float, 
                        help="reference CShM score if any",
                        default=0)               
    parser.add_argument('-o', 
                        dest='out', 
                        type=str, 
                        help="Output name file")

    args = parser.parse_args()
    
    tab_file = args.tab
    out_file = args.out
    coord = args.coord
    avg = args.avg
    plot = args.plot
    box = args.box
    ref = args.ref

    d_label={
        2:["Linear","Divacant tetrahedron","Tetravacant octahedron"],
        3:["Trigonal planar","Pyramid(vacant tetrahedron)","fac-Trivacant octahedron","mer-Trivacant octahedron"],
        4:["Square-planar", "Tetrahedral", "Seesaw", "V-trigonal-bipyramid"],
        5:["Pentagon","Vacant octahedron","Trigonal bipyramid","Square pyramid","Johnson trigonal bipyramid"],
        6:["Hexagon","Pentagonal pyramid","Octahedron","Trigonal prism","Johnson pentagonal pyramid"],
        7:["Heptagon","Hexagonal pyramid","Pentagonal bipyramid","Capped octahedron","Capped trigonal prism",
           "Johnson pentagonal bipyramid","Elongated triangular pyramid"],
        8:["Octagon","Heptagonal pyramid","Hexagonal bipyramid","Cube","Square antiprism","Triangular dodecahedron",
           "Johnson - Gyrobifastigium","Johnson - Elongated triangular bipyramid","Johnson - Biaugmented trigonal prism",
           "Biaugmented trigonal prism","Snub disphenoid","Triakis tetrahedron","Elongated trigonal bipyramid"],
        9:["Enneagon","Octagonal pyramid","Heptagonal bipyramid","Triangular cupola","Capped cube (Elongated square pyramid)",
           "Capped cube","Capped sq. antiprism","Capped square antiprism","Tricapped trigonal prism (J51)","Tricapped trigonal prism",
           "Tridiminished icosahedron (J63)","Hula-hoop","Muffin"],
        10:[],
        11:[],
        12:[],
        20:[],
        24:[],
        48:[],
        60:[]
        }
    
    data= parse_tab(tab_file)
    data.columns = d_label[coord]
    data=data.drop(columns=['Square-planar',])
    #data=data.drop(columns=["Hexagon","Pentagonal pyramid","Trigonal prism","Johnson pentagonal pyramid"])
    data.to_csv(out_file+".csv",sep='\t',index=False)
    if avg:
        data_avg = data.mean(axis=0).to_frame().T
        data_avg.to_csv(out_file+"_avg.csv",index='Average cshm score')
    if box:
        sns.boxplot(data=data)
        plt.ylabel("CSM")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("boxplot_%s.pdf" % out_file,dpi=300)
        plt.clf()
    if plot:
        
        for i in data:
            x = data.index.tolist()
            y = data[i]
            plt.plot(x,data[i], label=i, lw=0.5)
        if ref==0:
            pass
        else:
            plt.axhline(ref,ls='--',label='Reference')
        plt.xlabel("frame number")
        plt.ylabel("CShM")
        plt.xticks(rotation=45)
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.savefig("plot_%s.pdf" % out_file,dpi=300)
        plt.clf()



