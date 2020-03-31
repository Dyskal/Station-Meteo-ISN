from openpyxl import *
from openpyxl.styles import *
from os import getcwd
from Data import getData


def createXlsx():
    titres = ['Time', 'Temperature', 'Pressure', 'Humidity']
    pos = 0
    excel = Workbook()
    page = excel.active

    print('Fusion des cellules...')
    page.merge_cells('A1:B2')
    page.merge_cells('C1:D2')
    page.merge_cells('E1:F2')
    page.merge_cells('G1:H2')

    print('Création des titres...')
    for i in range(1, 9, 2):
        cell = page.cell(row=1, column=i)
        cell.value = titres[pos]
        cell.alignment = Alignment(horizontal='center', vertical='center')
        pos += 1

    excel.save(getcwd() + '\\python_weather_data.xlsx')
    print('Fichier créé !')


def updateXslx():
    data = getData()
    i = 3
    excel = load_workbook(getcwd() + '\\python_weather_data.xlsx')
    page = excel.active

    page.merge_cells('A' + str(i) + ':' + 'B' + str(i))
    page.merge_cells('C' + str(i) + ':' + 'D' + str(i))
    page.merge_cells('E' + str(i) + ':' + 'F' + str(i))
    page.merge_cells('G' + str(i) + ':' + 'H' + str(i))
    page['A' + str(i)] = data["Time"]
    page['C' + str(i)] = data["Temperature"]
    page['E' + str(i)] = data["Humidity"]
    page['G' + str(i)] = data["Pressure"]
    i += 1
    excel.save(getcwd() + '\\python_weather_data.xlsx')
    print('Mise à jour effectuée !')
