import xlsxwriter
from rozetka import array

def write(parametr):

    book = xlsxwriter.Workbook(r"C:\Users\s.fedoruk\Desktop\amazing\scraping\rozetka\rozetka.xlsx")
    page = book.add_worksheet('газовые плиты')

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        row += 1
    book.close()

write(array)