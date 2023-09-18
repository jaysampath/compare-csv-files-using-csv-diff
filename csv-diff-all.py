from csv_diff import load_csv, compare
from contextlib import redirect_stdout
import os as os
import csv
from pathlib import Path

prefix = "C:/path/"
result_file = "C:/path/differences/";

unique_column_name = 'USER_ID'

def find_differences(sub_folder_name):
    original_file_location = prefix + "original/" + sub_folder_name + "/"
    new_file_location = prefix + "new/" + sub_folder_name + "/"
    original_files = os.listdir(original_file_location)
    new_files = os.listdir(new_file_location)

    for f1 in original_files:
        for f2 in new_files:
            if f1 == f2.replace("new_", ""):
                print("comparing - ", f1, f2)
                with(open(original_file_location + f1, 'r')) as file1:
                    reader = csv.reader(file1, delimiter = ",")
                    data = list(reader)
                    row_count1 = len(data)
                with(open(new_file_location + f2, 'r')) as file2:
                    reader = csv.reader(file2, delimiter = ",")
                    data = list(reader)
                    row_count2 = len(data)
                print("Record counts: original_file=", row_count1, " and " "new_file=", row_count2)
                f1_load_with_key = load_csv(open(original_file_location + f1), key=unique_column_name)
                f2_load_with_key = load_csv(open(new_file_location + f2), key=unique_column_name)
                row_count_with_keys1 = len(f1_load_with_key)
                row_count_with_keys2 = len(f2_load_with_key)
                print("Record counts with key: original_file=", row_count_with_keys1, " and " "new_file=", row_count_with_keys2)
                difference = compare(f1_load_with_key, f2_load_with_key)
                #print(difference)
                with open(result_file + "diff_" + Path(f1).stem + ".json", 'w') as f:
                    with redirect_stdout(f):
                        print(difference)
                is_equal = len(difference.get('changed')) == 0 and len(difference.get('added')) == 0 and len(difference.get('removed')) == 0
                print("compared - ", f1, f2)
                if is_equal and row_count1 == row_count2 and row_count_with_keys1 == row_count_with_keys2:
                    print("data, record count and record count with keys are identical")
                else:
                    print("Not identical")
                print("--------")


folders = ["test1", "test2"]

for sub_folder in folders:
    find_differences(sub_folder_name=sub_folder)