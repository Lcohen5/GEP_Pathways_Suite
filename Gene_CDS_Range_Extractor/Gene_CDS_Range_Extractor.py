import pandas as pd

# Load your Excel file and change the name to correspond with the name of your file
file_path = 'your_file_name.xlsx'
#change to the sheet name that contains the data
df = pd.read_excel(file_path, sheet_name='sheetname')
df.columns = df.columns.str.strip()  # This Cleans column headers

# Step 1: This computes CDS range for each row
df['cds_range'] = df['end'] - df['start']

# Step 2: This get the row with the max range for each gene_id
max_rows = df.loc[df.groupby('gene_id')['cds_range'].idxmax()]

# Step 3: This saves result to a new Excel sheet
max_rows.to_excel('max_range_per_gene.xlsx', index=False)
print("\nSaved one row per gene_id with max CDS range to: max_range_per_gene.xlsx")


