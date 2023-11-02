import pandas as pd
import os
import openpyxl 

file_path = __file__
directory = os.path.dirname(file_path)

files = os.listdir(directory)

dict_general = {}

for i in files:
    if os.path.isdir(os.path.join(directory, i)):
        folder_path = os.path.join(directory, i)
        folder_contents = os.listdir(folder_path)
        print(i)
        dict_general[i] = {}
        for item in folder_contents:
            print(item)
            item_path = os.path.join(folder_path, item)
            wb = openpyxl.load_workbook(filename=item_path)
            sheet = wb.active

            carros = []
            kilos_x_carros = []

            for row in sheet.iter_rows(min_row=8,values_only=True):
                cell = row[0]
                if cell not in carros and cell != None and str(cell).isdigit():
                    carros.append(cell)
                    dict_general[i][item]
            
            print(carros)

            for carro in carros:
                dict_general[i][item][carro] = {'carro': carro}

            print(dict_general)
            dict_general[i][item] = {'a': 1}


print(dict_general)