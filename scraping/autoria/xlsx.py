import xlsxwriter
from auto import array
from auto_2 import content

def writer(parametr):
    book = xlsxwriter.Workbook(
        r"C:\Users\s.fedoruk\Desktop\amazing\scraping\autoria\file.xlsx"
    )
    page = book.add_worksheet("авто")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)
    page.set_column("E:E", 20)
    page.set_column("F:F", 20)
    # page.set_column("G:G", 20)
    # page.set_column("H:H", 20)
    # page.set_column("I:I", 20)
    # page.set_column("J:J", 20)
    # page.set_column("K:K", 20)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        page.write(row, column + 4, item[4])
        page.write(row, column + 5, item[5])
        # page.write(row, column + 6, item[6])
        # page.write(row, column + 7, item[7])
        # page.write(row, column + 8, item[8])
        # page.write(row, column + 9, item[9])
        # page.write(row, column + 10, item[10])
        row += 1

    book.close()

writer(content)