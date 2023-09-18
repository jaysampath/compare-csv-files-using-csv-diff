from csv_diff import load_csv, compare
from contextlib import redirect_stdout
import os as os

prefix = "C:/path/test/"

original_file = prefix + "file1.csv"
new_file = prefix + "file2.csv"

result_file = "C:/path/differences.json";

unique_column_name = 'USER_ID'


difference = compare(
    load_csv(open(original_file),key=unique_column_name),
    load_csv(open(new_file), key=unique_column_name)
)

#print(difference)


with open(result_file, 'w') as f:
    with redirect_stdout(f):
        print(difference)