# GMC_to_Apollo
This repository converts GFF files from the GEP Gene Model Checker into a format that can be uploaded to Apollo

Contents:
1. Input folder - Put all files you wish to convert here
2. Output folder - Find all of your converted files here
3. gff2_to_gff3.py - Use this python script to convert your files
4. DeleRefSeq2_sgg.gff = sample input file
5. DeleRefSeq2_sgg.gff3 = sample output file

Initial Setup:
1. Make sure you have python installed on your computer
2. Change lines 9 and 22 of gff2_to_gff3.py to reflect the input filepath on your local drive
3. Change lines 11 and 23 of gff2_to_gff3.py to reflect the output file path on your local drive
4. Save your changes
5. Put your input files into the input folder
6. Go into command line/terminal
7. Navigate to your directory's location using the cd command. For example:
   
  cd /Users/.../Apollo_Trackmaker/input
  
11. Run your code by entering the following into command line:
    
  python3 gff2_to_gff3.py

A succesful run with the sample input file will print the following:

Converting DeleRefSeq2_sgg.gff → DeleRefSeq2_sgg.gff3

🧬🪰 Congratulations! Your GFF file from the GEP Gene Model Checker has been converted. You can find the Apollo-ready file in your output foler. 🪰🧬

Patch by Katherine Warren (kkwarren27) on July 16, 2025: The patch resolves the issue of the GFF3 assigning the same "parent name" to all unique transcripts, which resulted in one combined mRNA of all unique transcripts. Instead now each transcript is separated into its own exons and CDSs.