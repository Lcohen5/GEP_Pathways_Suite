#!/usr/bin/env python3
from pathlib import Path

# Ask user for input folder and file type
input_dir = input("Enter the folder path with your sequence files: ").strip()
file_type = input("File type to combine (pep or fasta): ").strip().lower()
output_name = input("Enter the output filename (e.g., combined.pep): ").strip()

# Safety checks
if not output_name.endswith(f".{file_type}"):
    output_name += f".{file_type}"

input_path = Path(input_dir).expanduser().resolve()
files = sorted(input_path.glob(f"*.{file_type}"))

if not files:
    print(f"No .{file_type} files found in {input_path}")
    exit(1)

output_file = input_path / output_name

# Combine all files
with open(output_file, "w") as out:
    for file in files:
        with open(file, "r") as f:
            out.write(f.read())
            if not f.read().endswith('\n'):
                out.write('\n')  # Ensure newline between files

print(f" Combined {len(files)} files into: {output_file}")
