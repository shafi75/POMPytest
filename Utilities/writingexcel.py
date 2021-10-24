import openpyxl

path="..//excel//testexceldata.xlsx"
wb=openpyxl.load_workbook(path)
sheet=wb['testwrite']
for rows in range(1,4):
    for cols in range(1,4):
        sheet.cell(row=rows,column=cols).value="shafaat"

wb.save(path)