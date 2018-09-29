import os

load_path = '/home/thomas/Desktop/Snakemake/scripts/data/'
nameOfFile = "ID.txt"
completeName = os.path.join(load_path, nameOfFile)
f1 = open(completeName, "r")
ID = f1.readline()
    
    
from Bio.Blast import NCBIXML
result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)