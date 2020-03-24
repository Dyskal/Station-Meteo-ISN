from Data import getData
from tkinter import *
from sense_hat import SenseHat

sense = SenseHat()
data = getData()
main = Tk()

main.title('Station météo')
main.geometry('600x300')

timesv = StringVar()
timesv.set(data["Time"])
Time = Label(main, textvariable=timesv).pack()

tempsv = StringVar()
tempsv.set(data["Temperature"])
Temperature = Label(main, textvariable=tempsv).pack()

pressuresv = StringVar()
pressuresv.set(data["Pressure"])
Pressure = Label(main, textvariable=pressuresv).pack()

humiditysv = StringVar()
humiditysv.set(data["Humidity"])
Humidity = Label(main, textvariable=humiditysv).pack()

main.mainloop()
