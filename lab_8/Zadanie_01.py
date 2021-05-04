# Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel(pd.ExcelFile("datasets/imiona.xlsx"), "Arkusz1")
# print(df)