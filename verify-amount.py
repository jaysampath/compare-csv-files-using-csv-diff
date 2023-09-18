import os as os
import csv

prefix = "C:/path/"
result_file = "C:/path/differences/";

def verify_amount(sub_folder_name, first_column_no, second_column_no):
    original_file_location = prefix + "original/" + sub_folder_name + "/"
    new_file_location = prefix + "new/" + sub_folder_name + "/"
    original_files = os.listdir(original_file_location)
    new_files = os.listdir(new_file_location)
    for f1 in original_files:
        for f2 in new_files:
          if f1 == f2.replace("new_", ""):
            print("comparing - ", f1, f2)
            with open(original_file_location + f1, 'r') as file1:
                header = next(file1)
                number_column_1_original_file_sum = 0
                number_column_2_original_file_sum = 0
                for row in csv.reader(file1):
                    number_column_1_original_file_sum += float(row[first_column_no] or 0)
                    number_column_2_original_file_sum += float(row[second_column_no] or 0)
            with open(new_file_location + f2, 'r') as file2:
                header = next(file2)
                number_column_1_new_file_sum = 0
                number_column_2_new_file_sum = 0
                for row in csv.reader(file2):
                    number_column_1_new_file_sum += float(row[first_column_no] or 0)
                    number_column_2_new_file_sum += float(row[second_column_no] or 0)
            if number_column_1_original_file_sum == number_column_1_new_file_sum and number_column_2_original_file_sum == number_column_2_new_file_sum:
                print("both amounts are equal")
                print("Values-> number_column_1_sum- ", number_column_1_original_file_sum, number_column_1_new_file_sum, " number_column_2_sum", number_column_2_original_file_sum, number_column_2_new_file_sum)
            else:
                print("Values are unequal. number_column_1_sum- ", number_column_1_original_file_sum, number_column_1_new_file_sum, " number_column_2_sum", number_column_2_original_file_sum, number_column_2_new_file_sum)
            print("--------")


number_column_1_index = 9
number_column_2_index = 10

folders = ["test1", "test2"]

for sub_folder in folders:
    verify_amount(sub_folder_name=sub_folder, first_column_no=number_column_1_index, second_column_no=number_column_2_index)