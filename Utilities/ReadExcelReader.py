from Utilities import ExcelReader

path="..//excel//testexceldata.xlsx"
sheetname="testdata"
rows=ExcelReader.getRowCount(path,sheetname)
cols=ExcelReader.getColumnCount(path,sheetname)

print(ExcelReader.getCellData(path,sheetname,1,1))
