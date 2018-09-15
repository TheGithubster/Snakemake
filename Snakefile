"""
Created by: Thomas Reinders
Goal: Systematic information retrieval and insight in proteins and their function
Run: simply type: snakemake
"""

rule select_fasta:
    message:
        "<-- Starting file stream from root -->"
    script:
        'scripts/test.py'
 
