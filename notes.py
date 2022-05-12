CSV reader

   def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        with open(self.file.path, 'r') as f:

            import xlrd
            book = xlrd.open_workbook(self.file.path)
            sh = book.sheet_by_index(0)
            ly=[]
            lx=[]
            for x in range(sh.nrows):
                for y in range(sh.ncols):
                    lx.append(sh.cell_value(x, y))
                ly.append(lx)
                lx = []

            print(ly)
            pass



            rows = list(csv.reader(f))
            titles = rows[0]
            rows_except_title = rows[1:]
            print(rows)
            for i in rows_except_title:
                id = i[0]
                print(id)
                save_data = {c.strip(): j for c, j in zip(titles, i)}

                map(lambda l: [save_data.update({f'{n}_{l[0]}': n}) for n in titles if hasattr(Book, f'{n}_{l[0]}')], settings.LANGUAGES)

                Book.objects.filter(id=id).update(**save_data)












#############################################3
import xlrd

def main():
    
    file_path = ('/Users/akylbek/Desktop/test.xls')
    excel_workbook = xlrd.open_workbook(file_path)
    excel_sheet = excel_workbook.sheet_by_index(0)
    relevantData = [] 
    
    for row in range(excel_sheet.nrows): 
        if row % 2 != 0:
            relevantData.append(rowToArray(row))
        
        print(relevantData)

def rowToArray(row):
    return list(map(int, excel_sheet.cell_value(row,0).split()))



import xlrd
book = xlrd.open_workbook("/Users/akylbek/Desktop/test.xls")
sh = book.sheet_by_index(0)


print("Cell D30 is {0}".format(sh.cell_value(rowx=3, colx=3)))


for rx in range(sh.nrows):
    print(sh.row(rx))


import xlrd
book = xlrd.open_workbook("/Users/akylbek/Desktop/test.xls")
sh = book.sheet_by_index(0)

for x in range(sh.nrows):
    for y in range(sh.ncols):
            lx.append(sh.cell_value(x,y))
    ly.append(lx)
    lx=[]


[
    ['Место хранения',  '', '', 'Резерв', 'Свободный остаток'], 
    ['Номенклатура', ' Код', '', '', ''], 
    ['Склад Тунгуч', '', '', '', 842.0], 
    ['Зарыл суроо-жооптор 2', ' НФ-00000599', '', '', 79.0], 
    ['Берекелуу рамазан айы', ' НФ-00000569', '', '', 50.0], 
    ['Турмуш сабактары-7',    ' НФ-00000669', '', '', 36.0], 
    ['20 дуба кыска нуска',   ' НФ-00000521', '', '', 20.0], 
    ['40 хадис кыска нуска',  ' НФ-00000524', '', '', 20.0], 
    ['Куран (Тажвид)',        ' НФ-00000620', '', '', 20.0], 
    ['Оорулуга кат',          ' НФ-00000641', '', '', 20.0]
]


[
    ['Место хранения', '', 'Резерв', 'Свободный остаток'], 
    ['Номенклатура', ' Код', '', ''], 
    ['Склад Тунгуч', '', '', 12312.0], 

    ['Зарыл суроо-жооптор 2', ' НФ-00000599', 11.0, 51.0], 
    ['Берекелуу рамазан айы', ' НФ-00000569', 12.0, 52.0], 
    ['Турмуш сабактары-7', ' НФ-00000669', 13.0, 53.0], 
    ['20 дуба кыска нуска', ' НФ-00000521', 14.0, 54.0], 
    ['40 хадис кыска нуска', ' НФ-00000524', 15.0, 55.0], 
    ['Куран Алиппеси (Тажвид)', ' НФ-00000620', 16.0, 56.0], 
    ['Оорулуга кат', ' НФ-00000641', 17.0, 57.0]
]








        # idc = ly[3][1]
        # stleft = ly[3][4]

        # print(xls_content)
        # print(idc+"test")

        # test = Book.objects.filter(one_c_id=idc.strip())

        # test.update(stock= stleft)

        #
        # content = list(csv.reader(f))
        # names = content[0]
        # for i in content[1:]:
        #     # if i:
        #     title = i[0]
        #     save_data = {c: j for c, j in zip(names, i)}
        #
        #     if Book.objects.filter(title=title).exists():
        #         b = Book.objects.filter(title=title)
        #         b.update(
        #             **save_data
        #         )


            # with open(self.file.path, 'r') as f:
            # rows = list(csv.reader(f))
            # titles = rows[0]
            # rows_except_title = rows[1:]
            # print(rows)
            # for i in rows_except_title:
            #     id = i[0]
            #     print(id)
            #     save_data = {c.strip(): j for c, j in zip(titles, i)}
            #
            #     map(lambda l: [save_data.update({f'{n}_{l[0]}': n}) for n in titles if hasattr(Book, f'{n}_{l[0]}')], settings.LANGUAGES)
            #
            #     Book.objects.filter(id=id).update(**save_data)
