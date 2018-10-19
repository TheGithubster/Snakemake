from Bio import Entrez
import os.path

save_path = '/home/thomas/Desktop/Snakemake/scripts/data/'


#if you try running this script from a python shell, use: "data/ID.txt" as path
getIDs = open("scripts/data/ID.txt", "r")
id_list = []
for line in getIDs:
    line = line.replace("\n","").replace("\t","").replace("\w","")
    id_list.append(line)


Entrez.email = "Your.Name.Here@example.org"
handle = Entrez.efetch(db="protein", 
                       id=id_list, 
                       rettype="gb", #abstract or full article. whatever.
                       retmode="text") #xml
 

abstract = handle.read()
nameOfFile = "pubmed_annotation"
completeName = os.path.join(save_path, nameOfFile+".txt")
f = open(completeName, "w")
f.write(abstract)
handle.close()
f.close()

#abstract = handle.readlines()
#print(handle.readline().strip())


#f2 = open("data/pubmed_annotation.txt")
#for line in f2:
#    if "LOCUS" in line:
#       print(line)