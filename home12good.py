import openpyxl
import csv


with open('homework2.csv', 'r', encoding="utf-8") as csvfile:
    reader_file = csv.reader(csvfile)
    data = list(reader_file)


wb = openpyxl.Workbook()

new_list = wb.active

for i in data:
    new_list.append(i)

wb.save('myhomework1.xlsx')


wb = openpyxl.load_workbook('myhomework1.xlsx')

cools = wb.active

cools.delete_cols(3)

wb.save('done.xlsx')