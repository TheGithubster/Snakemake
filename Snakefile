"""
Created by: Thomas Reinders
Goal: Systematic information retrieval and insight in proteins and their function
Run: simply type: snakemake
""" 
report: "report/workflow.rst"


rule all:
    input: 
        "report.html"
   

rule select_fasta:
    message:
        "<-- Starting file stream from root -->"
    output:
        'copy.fa'
    script:
        'scripts/fastaloader.py'


rule blast:
    message:
        "<-- Starting blast -->"
    input:
         'copy.fa'
    output:
        'scripts/data/blast_results.out.txt',
        'scripts/data/blast_results.complete-visual-svg.svg'
    shell:
        'perl services/ncbiblast_lwp.pl --email "Thom-rein97@hotmail.nl" --sequence {input}' +
        ' --database "uniprotkb_bacteria" --stype protein --program blastp --align 7' +
        ' --alignments 5 --outfile scripts/data/blast_results' 

rule pubmed:
    message:
        "<-- Retrieving pubmed articles -->"
    input:
        'scripts/data/ID.txt'
    output:
        'scripts/data/pubmed_annotation.txt'
    script:
        'scripts/pubmed.py'

rule workflow:
    output:
        "workflow.svg"
    shell:
        "snakemake --dag all | dot -Tsvg > {output}"


rule report:
    message:
        "<-- Building an aesthetic overview -->"
    input: 
        'scripts/data/blast_results.complete-visual-svg.svg' 
        'scripts/data/pubmed_annotation.txt'
    output:
        'report.html'
    run:
        from snakemake.utils import report
        report("""OWE 11: Workflows""", output[0], output[1], metadata="Author: Reinders, Thomas", **input)



