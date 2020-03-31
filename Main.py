from Excel import *
from tkinter import *
# from sense_hat import SenseHat

# sense = SenseHat()
main = Tk()
createXlsx()

timesv = StringVar()
tempsv = StringVar()
pressuresv = StringVar()
humiditysv = StringVar()


def reloadData():
    data = getData()
    timesv.set("Date: " + data["Time"])
    tempsv.set("Température: " + data["Temperature"] + " °C")
    pressuresv.set("Pression: " + data["Pressure"] + " hPa")
    humiditysv.set("Humidité: " + data["Humidity"] + " %")
    updateXslx()


main.title('Station météo')
main.geometry('350x75')
reloadData()

Time = Label(main, textvariable=timesv)
Time.grid(row=0, column=0, columnspan=3)

Temperature = Label(main, textvariable=tempsv)
Temperature.grid(row=1, column=0)

Pressure = Label(main, textvariable=pressuresv)
Pressure.grid(row=1, column=1)

Humidity = Label(main, textvariable=humiditysv)
Humidity.grid(row=1, column=2)

Reload = Button(main, text="Recharger les données", command=reloadData)
Reload.grid(row=2, column=0, columnspan=3)

main.mainloop()
