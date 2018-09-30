
######## Snakemake header ########
import sys; sys.path.extend(["/home/thomas/miniconda3/lib/python3.6/site-packages", "/home/thomas/Desktop/Snakemake/scripts"]); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x05\x00\x00\x00inputq\x03csnakemake.io\nInputFiles\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x06\x00\x00\x00outputq\tcsnakemake.io\nOutputFiles\nq\n)\x81q\x0b}q\x0ch\x07}q\rsbX\x06\x00\x00\x00paramsq\x0ecsnakemake.io\nParams\nq\x0f)\x81q\x10}q\x11h\x07}q\x12sbX\t\x00\x00\x00wildcardsq\x13csnakemake.io\nWildcards\nq\x14)\x81q\x15}q\x16h\x07}q\x17sbX\x07\x00\x00\x00threadsq\x18K\x01X\t\x00\x00\x00resourcesq\x19csnakemake.io\nResources\nq\x1a)\x81q\x1b(K\x01K\x01e}q\x1c(h\x07}q\x1d(X\x06\x00\x00\x00_coresq\x1eK\x00N\x86q\x1fX\x06\x00\x00\x00_nodesq K\x01N\x86q!uh\x1eK\x01h K\x01ubX\x03\x00\x00\x00logq"csnakemake.io\nLog\nq#)\x81q$}q%h\x07}q&sbX\x06\x00\x00\x00configq\'}q(X\x04\x00\x00\x00ruleq)X\x0c\x00\x00\x00select_fastaq*ub.'); from snakemake.logging import logger; logger.printshellcmds = False
######## Original script #########
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import re
import os.path

save_path = '/home/thomas/Desktop/Snakemake/scripts/data/'

def main():
    self = Tk()

    F1 = LabelFrame(self, text="Select File")
    F1.grid(row=0, column=0, padx=3)

    browse = Button(F1, text="Browse...", command=openfile)
    browse.grid(row=0, column=2, padx=1, pady=3)

    L1 = Label(F1, text="Filename:")
    L1.grid(row=0, column=0, padx=3)

    B1 = Button(F1, text="Use This File", command=go)
    B1.grid(row=1, column=2, padx=3, pady=3)

    B2 = Button(F1, text="Cancel", width=7)
    B2.grid(row=1, column=1, sticky="e")

    self.mainloop()

def openfile():
    global filename
    filename = filedialog.askopenfilename() 

def go():
    global filename
    file = open(filename)
    file_content = file.readlines()
    print("loading identifiers from selected file...")
    for line in file_content:
        if "|" in line:
            result = re.search('(?<=\|)(.*?)(?=\|)', line)
            resultString = result.group(1)
            print("saving identifiers: " + resultString + " in ID.txt...")
            nameOfFile = "ID"
            completeName = os.path.join(save_path, nameOfFile+".txt")
            f1 = open(completeName, "w")
            f1.write(resultString + "\n")
            f1.close()
    
    file.close()
        
    
main()