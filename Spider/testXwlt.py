import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1") #创建工作表

content = worksheet.write(0,0,"hello")
workbook.save("student.xls")



