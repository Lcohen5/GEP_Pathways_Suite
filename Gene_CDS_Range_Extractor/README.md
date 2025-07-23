**🧬 Gene CDS Range Extractor**

A Python script that reads an Excel spreadsheet of gene data and extracts the row with the largest CDS range (end - start) for each gene_id. It saves the results to a new .xlsx file with full metadata (like scaffold and strand) preserved.

**📦 Features**
- Supports .xlsx Excel files
- Customize input file name and sheet
- Calculates one row per gene_id with maximum CDS span
- Preserves all original columns
- Saves result as max_range_per_gene.xlsx

**🧪 Example Input Format**

Your Excel sheet should include at least the following columns of information:

gene_id, start, end, scaffold, strand


**🛑 Before you get started**
1. Install Python (if not already installed):
Get it here: https://www.python.org/downloads

2. Place your input Excel file (e.g., your_genes.xlsx) in the same folder as the script.

3. Open the .py script and follow the instructions to modify the code to your specific Excel name & sheet. 

4. Open Terminal and orient to the Gene_CDS_Range_Extractor using the cd Command:

cd /path/to/your/script

5. Create a virtual environment in Terminal:

python3 -m venv venv

6. To activate virtual environement:
   
**for macOS only**

source venv/bin/activate 

**for Windows only**

venv\Scripts\activate     

7. Install required library to open Excel files:

python3 -m pip install pandas openpyxl

**😎To Use:**

8. Run the script:

python3 Gene_CDS_Range_Extractor.py

**Yay you did it!** 🥳 

The output will be saved as:
max_range_per_gene.xlsx


