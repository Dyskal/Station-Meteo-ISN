from openpyxl import *
from openpyxl.styles import *
from os import getcwd
from Data import getData

line = 3


def createXlsx():   # Cette fonction permet de créer le fichier excel
    titres = ['Date', 'Température', 'Pression', 'Humidité']  # On définit les titres
    pos = 0
    excel = Workbook()
    page = excel.active

    print('Fusion des cellules...')  # On fusionne les cellules de titre
    page.merge_cells('A1:B2')
    page.merge_cells('C1:D2')
    page.merge_cells('E1:F2')
    page.merge_cells('G1:H2')

    print('Création des titres...')  # On crée les titres dans les cellules fusionnées
    for i in range(1, 9, 2):
        cell = page.cell(row=1, column=i)
        cell.value = titres[pos]
        cell.alignment = Alignment(horizontal='center', vertical='center')
        pos += 1

    excel.save(getcwd() + '\\python_weather_data.xlsx')
    print('Fichier créé !')


def updateXslx():   # Cette fonction permet de mettre à jour le fichier excel
    global line
    data = getData()
    excel = load_workbook(getcwd() + '\\python_weather_data.xlsx')
    page = excel.active

    page.merge_cells('A' + str(line) + ':' + 'B' + str(line))
    page.merge_cells('C' + str(line) + ':' + 'D' + str(line))
    page.merge_cells('E' + str(line) + ':' + 'F' + str(line))
    page.merge_cells('G' + str(line) + ':' + 'H' + str(line))
    page['A' + str(line)] = data["Time"]
    page['C' + str(line)] = data["Temperature"]
    page['E' + str(line)] = data["Pressure"]
    page['G' + str(line)] = data["Humidity"]
    line += 1
    excel.save(getcwd() + '\\python_weather_data.xlsx')
    print('Mise à jour effectuée !')
