#!/usr/bin/env python3

import csv
import os

# List all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.lower().endswith('.csv')]

# If no CSVs found
if not csv_files:
    print("No CSV files found in the current directory.")
    exit()

# Display options
print("Available CSV files:")
for i, file in enumerate(csv_files, 1):
    print(f"{i}. {file}")

# Let user choose one
choice = input("Enter the number of the CSV file to use: ")
try:
    selected_file = csv_files[int(choice) - 1]
except (IndexError, ValueError):
    print("Invalid selection.")
    exit()

# Get exon list from user
user_input = input("Enter exon numbers to include (comma-separated, e.g. 1,3,5,6): ")
selected_exons = {x.strip() for x in user_input.split(",")}

coordinates = []

# Open selected CSV with BOM-safe encoding
with open(selected_file, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    try:
        for row in reader:
            exon_id = row["Exon_ID"]
            if exon_id in selected_exons:
                start = row["Start_Coordinate"]
                end = row["End_Coordinate"]
                coordinates.append(f"{start}-{end}")
    except KeyError as e:
        print(f"Missing expected column: {e}")
        exit()

# Output result
if coordinates:
    print(f"\n🧬 Success! 🪰 Here are the coordinates for your selected exons from {selected_file}:")
    print(", ".join(coordinates))
else:
    print("\nNo matching exons found.")
