import os
import openpyxl


path = r"C:\Users\Sinclair\Desktop\python\PYTHON-learn\excel"
os.chdir(path)

work_book = openpyxl.load_workbook('test.xlsx')
print(work_book.active)