#Text Files
#  with open('file1.txt', 'w') as file:
#     file.write("Hello world!")
#Reading
with open('file1.txt', 'r') as file:
    content = file.read()
    print(content)

#CsV Files simple method just like the txt file
import csv
with open('Sample2.csv', 'r') as file:  
     variable=  file.read()
     print(variable)

#DictReader Method
import csv
with open('Sample2.csv', 'r') as file:
    content = csv.DictReader(file)
    for row in content:
        print(row)

#Using Reader
import csv
with open('Sample.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
        # print(row[2])     # to call any specific value mention index


# writerows:
  # Multiple rows at once.
import csv
# Write to the CSV file
with open('sample2.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Country'])  # Writing headers

    rows = [
        ['Charlie', '28', 'America'],
        ['David', '35', 'India']
    ]
    writer.writerows(rows)

# Read and display the contents of the CSV file
with open('sample2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

