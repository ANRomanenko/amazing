import xlsxwriter
from allo import array

def write(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\s.fedoruk\Desktop\amazing\scraping\allo\all.xlsx")
    page = book.add_worksheet("ноуты")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)
    page.set_column("E:E", 20)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        row += 1

    book.close()

write(array)