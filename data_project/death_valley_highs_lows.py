import csv

filename = "/Users/malte.niepel/Desktop/mniepel/ehmatthes-pcc_2e-078318e/chapter_16/the_csv_file_format/data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
