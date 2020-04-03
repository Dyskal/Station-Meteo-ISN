from Excel import *
from tkinter import *
from os import path, getcwd
# from sense_hat import SenseHat

# sense = SenseHat()
main = Tk()     # On crée une fenetre tkinter
if not path.exists(getcwd() + '\\python_weather_data.xlsx'):    # On vérifie si le fichier excel existe
    createXlsx()                                                # Sinon on le crée

timesv = StringVar()        # On définit des chaines de caractère variables pour les labels tkinter
tempsv = StringVar()
pressuresv = StringVar()
humiditysv = StringVar()


def reloadData():       # Cette fonction permet de mettre à jour les données météo
    data = getData()
    timesv.set("Date: " + data["Time"])
    tempsv.set("Température: " + data["Temperature"] + " °C")
    pressuresv.set("Pression: " + data["Pressure"] + " hPa")
    humiditysv.set("Humidité: " + data["Humidity"] + " %")
    updateXslx()        # Et ensuite de mettre les valeurs dans le fichier Excel


main.title('Station météo')
main.geometry('350x75')
reloadData()

Time = Label(main, textvariable=timesv)     # On crée un label qui affiche la date
Time.grid(row=0, column=0, columnspan=3)

Temperature = Label(main, textvariable=tempsv)      # On crée un label qui affiche la température
Temperature.grid(row=1, column=0)

Pressure = Label(main, textvariable=pressuresv)     # On crée un label qui affiche la pression
Pressure.grid(row=1, column=1)

Humidity = Label(main, textvariable=humiditysv)     # On crée un label qui affiche l'humidité
Humidity.grid(row=1, column=2)

Reload = Button(main, text="Recharger les données", command=reloadData)
# On crée un boutton qui permet de recharger les données
Reload.grid(row=2, column=0, columnspan=3)

main.mainloop()
