#!/usr/bin/env python3
"""
This program will convert the output of the GEP Gene Model Checker (GFF2) that are
in the input folder into a GFF3 format that suitable for user-level upload to Apollo.

The output files will emit only mRNA and its child features (no separate gene entries).

Input directory:
  /Users/.../Apollo_Trackmaker/input
Output directory:
  /Users/.../Apollo_Trackmaker/input

To activate this code:
  chmod +x gff2_to_gff3.py
To run this code:
  ./gff2_to_gff3.py
"""
import os
import re

# Configure paths
INPUT_DIR = "/Users/.../Apollo_Trackmaker/input"
OUTPUT_DIR = "/Users/.../Apollo_Trackmaker/input"
OUTPUT_EXT = ".gff3"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_attributes(attr_str):
    """Convert GFF2 attributes to GFF3 key=value;key2=value2 format."""
    pattern = re.compile(r'(\S+?)\s*\"([^\"]*)\"|(\S+?)=(\S+)')
    attrs = []
    for m in pattern.finditer(attr_str):
        if m.group(1) and m.group(2) is not None:
            key, val = m.group(1), m.group(2)
        else:
            key, val = m.group(3), m.group(4)
        attrs.append(f"{key}={val}")
    return ';'.join(attrs)

def parse_gff2(path):
    """Parse GFF2 file, return seqid, min_start, max_end, strand, and feature list."""
    features = []
    starts, ends = [], []
    seqid = None
    strand = None
    with open(path) as fin:
        for line in fin:
            if line.startswith('track') or line.startswith('##') or line.startswith('#'):
                continue
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 9:
                continue
            sid, source, ftype, start, end, score, sd, phase, attr_str = cols
            seqid = sid
            s, e = int(start), int(end)
            starts.append(s)
            ends.append(e)
            strand = sd
            attr_str3 = convert_attributes(attr_str)
            features.append((ftype, s, e, score, strand, phase, attr_str3))
    return seqid, min(starts), max(ends), strand, features

def write_gff3(path, base, seqid, start, end, strand, features):
    """Write GFF3: only mRNA and its CDS/exon children."""
    mrna_id = f"{base}-PA"
    with open(path, 'w') as fout:
        fout.write("##gff-version 3\n")
        fout.write(f"##sequence-region {seqid} {start} {end}\n")
        # mRNA feature
        fout.write(
            f"{seqid}\t.\tmRNA\t{start}\t{end}\t.\t{strand}\t.\t"
            f"ID={mrna_id};transcript_id={mrna_id}\n"
        )
        # child features
        for ftype, s, e, score, sd, phase, attrs in features:
            if ftype not in ("CDS", "exon"):
                continue
            fout.write(
                f"{seqid}\tGEP\t{ftype}\t{s}\t{e}\t{score}\t{sd}\t{phase}\t"
                f"Parent={mrna_id};{attrs}\n"
            )
        fout.write("###\n")

def main():
    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith('.gff') and not f.lower().endswith(OUTPUT_EXT)
    ]
    if not files:
        print(f"No GFF2 files found in {INPUT_DIR}")
        return

    for fname in files:
        base = os.path.splitext(fname)[0]
        in_path = os.path.join(INPUT_DIR, fname)
        out_fname = base + OUTPUT_EXT
        out_path = os.path.join(OUTPUT_DIR, out_fname)
        print(f"Converting {fname} → {out_fname}")
        seqid, start, end, strand, feats = parse_gff2(in_path)
        write_gff3(out_path, base, seqid, start, end, strand, feats)

    print("🧬🪰 Congratulations! Your GFF file from the GEP Gene Model Checker has been converted. You can find the Apollo-ready file in your output foler. 🪰🧬")

if __name__ == '__main__':
    main()
