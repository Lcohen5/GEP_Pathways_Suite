#!/usr/bin/env python3
"""
Convert GEP Gene Model Checker GFF2 files to Apollo-compatible GFF3 format.
Handles multiple isoforms correctly, assigning features to the proper transcript.

Input directory:
  /Users/katherinewarren/Documents/Summer_2025_Reconciliation/Reference_Materials/GMC_to_Apollo/Input

Output directory:
  /Users/katherinewarren/Documents/Summer_2025_Reconciliation/Reference_Materials/GMC_to_Apollo/Output

To activate:
  chmod +x gff2_to_gff3.py
To run:
  ./gff2_to_gff3.py
"""

import os
import re

# ====== Configuration ======
INPUT_DIR = "/Users/katherinewarren/Documents/Summer_2025_Reconciliation/Reference_Materials/GMC_to_Apollo/Input"
OUTPUT_DIR = "/Users/katherinewarren/Documents/Summer_2025_Reconciliation/Reference_Materials/GMC_to_Apollo/Output"
OUTPUT_EXT = ".gff3"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_attributes(attr_str):
    """Convert GFF2 attributes to GFF3 format: key=value;key2=value2."""
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
    """Parse GFF2 and group features by transcript_id."""
    transcripts = {}
    with open(path) as fin:
        for line in fin:
            if line.startswith('track') or line.startswith('#'):
                continue
            cols = line.rstrip('\n').split('\t')
            if len(cols) < 9:
                continue
            seqid, source, ftype, start, end, score, strand, phase, attr_str = cols
            s, e = int(start), int(end)
            attr_str3 = convert_attributes(attr_str)
            match = re.search(r'transcript_id=([^;]+)', attr_str3)
            if not match:
                continue
            tid = match.group(1)
            if tid not in transcripts:
                transcripts[tid] = {
                    "features": [],
                    "start": s,
                    "end": e,
                    "strand": strand,
                    "seqid": seqid
                }
            transcripts[tid]["features"].append((ftype, s, e, score, strand, phase, attr_str3))
            transcripts[tid]["start"] = min(transcripts[tid]["start"], s)
            transcripts[tid]["end"] = max(transcripts[tid]["end"], e)
    return transcripts

def write_gff3(path, transcripts):
    """Write a GFF3 file for multiple transcripts with proper structure."""
    with open(path, 'w') as fout:
        fout.write("##gff-version 3\n")
        for tid, data in transcripts.items():
            seqid = data["seqid"]
            start = data["start"]
            end = data["end"]
            strand = data["strand"]
            features = data["features"]
            fout.write(f"##sequence-region {seqid} {start} {end}\n")
            fout.write(
                f"{seqid}\t.\tmRNA\t{start}\t{end}\t.\t{strand}\t.\t"
                f"ID={tid};transcript_id={tid}\n"
            )
            for ftype, s, e, score, sd, phase, attrs in features:
                if ftype not in ("CDS", "exon"):
                    continue
                fout.write(
                    f"{seqid}\tGEP\t{ftype}\t{s}\t{e}\t{score}\t{sd}\t{phase}\t"
                    f"Parent={tid};{attrs}\n"
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
        transcripts = parse_gff2(in_path)
        write_gff3(out_path, transcripts)

    print("🧬🪰 Done! All GFF2 files have been converted to GFF3 format with isoforms properly handled. 🪰🧬")

if __name__ == '__main__':
    main()
