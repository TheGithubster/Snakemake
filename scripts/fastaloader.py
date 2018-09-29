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
    for line in file_content:
        if "|" in line:
            print("loading identifiers from selected file...")
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