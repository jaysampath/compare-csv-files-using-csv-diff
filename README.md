# compare-csv-files-using-csv-diff

This project provides python scripts to compare csv files for data parity, record count etc. This project uses rich python libraries such as `csv-diff`, `csv` etc.

### sort-csv-files.py
* Takes the csv files sorts it in place based on the coloumn indices provided and writes sorted data in the same file
* uses csv library

### csv-diff-all.py
* Compares two files in different directories and prints the differences in records in another json file
* Place your to be compared files in "original" and "new" folder and run the script
* Uses csv-diff library

### verify-amount.py
* Helps in comparing sum of a number column in two different csv files
* Uses csv library