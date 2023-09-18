import csv
import os

prefix = "C:/path/staging/"
input_files = os.listdir(prefix)

sort_primary_column_index = 13
sort_secondary_column_index = 25

for f in input_files:
    #Read
    f = prefix + f
    with open(f, 'r') as file:
        data = list(csv.reader(file))
        header = data[0]
        sorted_data = sorted(data[1:], key=lambda row: (row[sort_primary_column_index], row[sort_secondary_column_index]))
    #Write
    with open(f, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(sorted_data)

    print("sorted file -", f)