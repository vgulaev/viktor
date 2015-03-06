import xlrd
rb = xlrd.open_workbook("PRICE_ARS.XLS",formatting_info=True)
sheet = rb.sheet_by_index(0)
"""
for row_index in range(ws.nrows):
    vendor = ws.row(row_index)[2].value
    part_number = ws.row(row_index)[4].value
    description = ws.row(row_index)[5].value
    price = ws.row(row_index)[8].value
    print (vendor, part_number, description, repr(price))
"""
for i in range(5):
    print(sheet.cell(i,2).value)
print("Everything ok")
