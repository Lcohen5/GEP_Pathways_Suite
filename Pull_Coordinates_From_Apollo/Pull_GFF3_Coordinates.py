#!/usr/bin/env python3
import os
from collections import defaultdict
import re

#Built by Logan Cohen, with some behind-the-scenes debugging magic from Lyric (an AI who drinks code for breakfast — courtesy of OpenAI).

#This tool was developed with the support of AI assistance to model collaborative and ethical technology use. Remember to apply the same critical thinking you use when evaluating computer-generated gene models during annotation to any other AI-assisted work you do. Always double-check results, think critically, and take ownership of your learning. AI can help you explore — but it should never replace your voice, your judgment, or your creativity.

#🧬🪰 Logan Cohen  
#🦉✨ Lyric

#Identify only the GFF files in the target folder and print a list of GFF files for the user to select
def list_gff_files():
    return [f for f in os.listdir() if f.endswith((".gff", ".gff3"))]

def choose_file(gff_files):
    print("Select a GFF3 file:")
    for i, file in enumerate(gff_files, 1):
        print(f"{i}: {file}")
    choice = int(input("Which file would you like to process? Enter the number and press enter: "))
    return gff_files[choice - 1]

#extract the isoform name and coordinates from the GFF3 file, cleaning up extraneous information before printing
def extract_cds_coordinates(file_path):
    id_to_name = {}
    cds_by_isoform = defaultdict(list)

    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) != 9:
                continue
            feature_type = parts[2]
            start = int(parts[3])
            end = int(parts[4])
            attributes = parts[8]
            attr_dict = dict(item.split("=", 1) for item in attributes.split(";") if "=" in item)

            if feature_type in ("mRNA", "transcript") and "ID" in attr_dict and "Name" in attr_dict:
                full_name = attr_dict["Name"]
                name_no_prefix = full_name.split(".", 1)[-1]  # remove "VELAZQUEZ-ULLOA." or similar
                clean_name = re.sub(r"-\d+$", "", name_no_prefix)  # remove trailing -00008
                id_to_name[attr_dict["ID"]] = clean_name

        f.seek(0)
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) != 9:
                continue
            feature_type = parts[2]
            start = int(parts[3])
            end = int(parts[4])
            attributes = parts[8]
            attr_dict = dict(item.split("=", 1) for item in attributes.split(";") if "=" in item)

            if feature_type == "CDS" and "Parent" in attr_dict:
                for parent_id in attr_dict["Parent"].split(","):
                    isoform_name = id_to_name.get(parent_id)
                    if isoform_name:
                        cds_by_isoform[isoform_name].append((start, end))

    return cds_by_isoform

#print out the results, including feedback for common processing errors
def main():
    gff_files = list_gff_files()
    if not gff_files:
        print("No GFF3 files found in the current directory.")
        return

    selected_file = choose_file(gff_files)
    print(f"\nProcessing file: {selected_file}\n")

    cds_coords = extract_cds_coordinates(selected_file)

    for isoform, coords in sorted(cds_coords.items()):
        print(f"{isoform}:")
        for start, end in sorted(set(coords)):
            print(f"  {start}-{end}")
        print()

if __name__ == "__main__":
    main()
