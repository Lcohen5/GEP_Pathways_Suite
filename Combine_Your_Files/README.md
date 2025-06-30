# FASTA/PEP File Collator

This lightweight script combines multiple `.fasta` or `.pep` files into a single output file using **plain Python** — no dependencies, no setup headaches.

---

## Requirements

- Python 3.0+ 
- A folder containing `.pep` or `.fasta` files  
- No external libraries required

---

## How to Use

1. Open Terminal  
2. Navigate to the folder containing the script:

    ```bash
    cd /path/to/your/script
    ```

3. Run the script:

    ```bash
    python3 FASTA_Peptide_Collator.py
    ```

4. Follow the prompts:
   - Enter the folder path containing your `.pep` or `.fasta` files
   - Choose file type (`pep` or `fasta`)
   - Enter a name for the combined output file

---

## Example

If you have this folder:

```
/Users/yourname/Desktop/Sequences/
├── Dana_chico.pep
├── Dmoj_chico.pep
├── Dgri_chico.pep
```

And run the script from Terminal, it will generate:

```
/Users/yourname/Desktop/Sequences/combined.pep
```

---

## Features

- Prompts for input directory, file type, and output filename  
- Combines files in alphabetical order  
- Preserves original FASTA headers and formatting  
- Ensures newline between concatenated files

---

## No Biopython or Pip Needed

This version is 100% compatible with fresh Python 3 installs — ideal for classrooms, teaching, or minimalist setups.

---

## Tip

If you just want to combine files from the command line (no script), you can do:

```bash
cat *.pep > combined.pep
```

But this script gives you more control and works cross-platform.

---
