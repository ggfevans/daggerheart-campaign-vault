import os
import csv
import tempfile
import shutil

csv_dir = "csv"

for filename in os.listdir(csv_dir):
    if filename.lower().endswith(".csv"):
        filepath = os.path.join(csv_dir, filename)
        temp_path = filepath + ".tmp"

        with open(filepath, "r", encoding="utf-8-sig", newline="") as infile, open(
            temp_path, "w", encoding="utf-8-sig", newline=""
        ) as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                new_row = [
                    field.replace("\\n", "\n") if field else field for field in row
                ]
                writer.writerow(new_row)

        shutil.move(temp_path, filepath)
        print(f"Updated: {filepath}")
