"""
Created by: Thomas Reinders
Goal: Systematic information retrieval and insight in proteins and their function
Run: simply type: snakemake
""" 
report: "report/workflow.rst"

rule all:
    input: "report.html"

rule select_fasta:
    message:
        "<-- Starting file stream from root -->"
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
    script:
        'scripts/pubmed.py'

rule report:
    message:
        "<-- Building an aesthetic overview -->"
    input:
        'scripts/data/blast_results.complete-visual-svg.svg'
    output:
        'report.html'
    script:
        'scripts/report_parser.py'




