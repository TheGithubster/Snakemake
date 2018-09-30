#import os
#load_path = '/home/thomas/Desktop/Snakemake/scripts/data/'
#nameOfFile = "ID.txt"
#completeName = os.path.join(load_path, nameOfFile)
#f1 = open(completeName, "r")
#ID = f1.readline()
    
f = open("path.txt","r")
for line in f:
    print(line)
    