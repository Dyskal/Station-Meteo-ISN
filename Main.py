from Data import getData
from tkinter import *
# from sense_hat import SenseHat

# sense = SenseHat()
data = getData()
main = Tk()

main.title('Station météo')
main.geometry('350x50')

timesv = StringVar()
timesv.set("Date: " + data["Time"])
Time = Label(main, textvariable=timesv)
Time.grid(row=0, column=0, columnspan=3)

tempsv = StringVar()
tempsv.set("Température: " + data["Temperature"] + " °C")
Temperature = Label(main, textvariable=tempsv)
Temperature.grid(row=1, column=0)

pressuresv = StringVar()
pressuresv.set("Pression: " + data["Pressure"] + " hPa")
Pressure = Label(main, textvariable=pressuresv)
Pressure.grid(row=1, column=1)

humiditysv = StringVar()
humiditysv.set("Humidité: " + data["Humidity"] + " %")
Humidity = Label(main, textvariable=humiditysv)
Humidity.grid(row=1, column=2)

main.mainloop()
