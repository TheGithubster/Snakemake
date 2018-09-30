from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import re
import os.path
import yaml

save_path = '/home/thomas/Desktop/Snakemake/scripts/data/'
save_path_config = '/home/thomas/Desktop/Snakemake/'

def main():
    self = Tk()

    F1 = LabelFrame(self, text="Select File")
    F1.grid(row=0, column=0, padx=3)

    browse = Button(F1, text="Browse...", command=openfile)
    browse.grid(row=0, column=2, padx=1, pady=3)

    L1 = Label(F1, text="1) Browse File")
    L1.grid(row=0, column=0, padx=3)
    
    L2 = Label(F1, text="2) Click 'Use this file'")
    L2.grid(row=1, column=0, padx=3)
    
    L3 = Label(F1, text="3) Close GUI")
    L3.grid(row=2, column=0, padx=3)

    B1 = Button(F1, text="Use This File", command=go)
    B1.grid(row=1, column=2, padx=1, pady=3)

 #   B2 = Button(F1, text="Cancel", width=7)
 #   B2.grid(row=1, column=1, sticky="e")

    
    self.mainloop()
    
def openfile():
    global filename
    try:
        filename = filedialog.askopenfilename() 
    except:
        print("No file selected")

def go():
    try:
        global filename
                    
        file = open(filename)
        file_content = file.readlines()
        
        print("saving identifiers...")
        for line in file_content: 
            if "|" in line:
                result = re.search('(?<=\|)(.*?)(?=\|)', line)
                resultString = result.group() 
                print(resultString) #mp fasta not included
                nameOfFile = "ID"
                completeName = os.path.join(save_path, nameOfFile+".txt")
                f1 = open(completeName, "w")
                f1.write(resultString + "\n")
            f1.close()
              
        file.close()
        file_content = open(filename, "r")
        f2 = open("copy.fa", "w")
        for line in file_content:
            f2.write(line)
        f2.close()
    except:
        print("No file selected")
        
    
main()