import xlrd
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
print (ROOT_DIR)
xlsxFileLocation = ROOT_DIR + '\\files\\input.xlsx'
txtOutputFile = ROOT_DIR + '\\files\\output.txt'

strToAppend = "kget "
strTemp =''

# intilize a null list
unique_list = []

# Open a workbook
workbook = xlrd.open_workbook(xlsxFileLocation)

# Load a specific sheet by name
worksheet = workbook.sheet_by_index(0)

# Get total no rows in the workbook
rowsCnt = worksheet.nrows

print("Total number of rows in excel file : " + str(rowsCnt))

# Open output text file
f = open(txtOutputFile,'w+')

for i in range(1,rowsCnt):
    cellValue = str(worksheet.cell_value(i,1)).split("=")[0]
    if strTemp != cellValue:
        strTemp = cellValue
        if cellValue not in unique_list:
            unique_list.append(cellValue)
            print(cellValue)

for cell in unique_list:
 f.write(strToAppend + cell + '\n')

f.close()