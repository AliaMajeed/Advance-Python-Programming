# 1. TXT Files
# Normal text files (.txt)
# Read/Write using simple open modes (r, w, a, etc.)
# If the file has no data means empty, open it in write mode ('w') to add something first.
# If the file already has content, open it in read mode ('r') and just read it.

#Writing
with open('file.txt', 'w') as file:
    file.write("Hello world!")
#Reading
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)


# 2. CSV Files (Comma Separated Values) CSV: rows and columns
# Special text files where data is separated by commas.
# We use csv module to work with CSV files.
# ➔ Reader:
# Reads data line by line.

import csv
with open('Sample.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        # print(row)
        print(row[2])     # to call any specific value mention index


#DictReader:
#Reads CSV into a dictionary (column names as keys).
# reads the CSV file and treats each row as a dictionary.
import csv
with open('Sample.csv', 'r') as file:
    content = csv.DictReader(file)
    for row in content:
        print(row)
      