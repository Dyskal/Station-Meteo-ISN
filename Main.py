from tkinter import StringVar, PhotoImage
from tkinter.ttk import Label, Button
from ttkthemes import ThemedTk, ThemedStyle
from Excel import updateXslx, excelwb
# from sense_hat import SenseHat

main = ThemedTk(background=True, theme="equilux")  # On crée une fenetre tkinter
angle = 90  # On attribue manuellement un angle pour tester

# sense = SenseHat()
timesv = StringVar()  # On définit des chaines de caractère variables pour les labels tkinter
tempsv = StringVar()
pressuresv = StringVar()
humiditysv = StringVar()
dirsv = StringVar()


def sense():  # Boucle pour recevoir les appuis du joystick et la direction de la boussole
    # angle = sense.get_compass()
    global angle
    if angle < 45 or angle > 315:
        dirsv.set('Nord')
        # sense.set_rotation(90)
    elif angle < 135:
        dirsv.set('Est')
        # sense.set_rotation(0)
    elif angle < 225:
        dirsv.set('Sud')
        # sense.set_rotation(270)
    else:
        dirsv.set('Ouest')
        # sense.set_rotation(180)
    # sense.show_letter(dirsv.get()[0])
    # angle += 20
    main.after(1000, sense)


def reloadData():  # Cette fonction permet de mettre à jour les données météo
    from Data import getData
    data = getData()
    timesv.set("Date: " + data["Time"])
    tempsv.set("Température: " + data["Temperature"] + " °C")
    pressuresv.set("Pression: " + data["Pressure"] + " hPa")
    humiditysv.set("Humidité: " + data["Humidity"] + " %")
    sense()
    updateXslx()  # Et ensuite de mettre les valeurs dans le fichier Excel


def close():  # Fonction pour fermer la fenetre correctement
    main.destroy()
    excelwb.close()


# sense.stick.direction_any = reloadData

main.title('Station météo')
main.geometry('350x100')
main.iconphoto(True, PhotoImage(file="resources/icon.png"))
style = ThemedStyle(main)
main.protocol('WM_DELETE_WINDOW', close)
reloadData()

Time = Label(main, textvariable=timesv)  # On crée un label qui affiche la date
Time.grid(row=0, column=0, columnspan=3)

Temperature = Label(main, textvariable=tempsv)  # On crée un label qui affiche la température
Temperature.grid(row=1, column=0)

Pressure = Label(main, textvariable=pressuresv)  # On crée un label qui affiche la pression
Pressure.grid(row=1, column=1)

Humidity = Label(main, textvariable=humiditysv)  # On crée un label qui affiche l'humidité
Humidity.grid(row=1, column=2)

Reload = Button(main, text="Recharger les données", command=reloadData)
# On crée un boutton qui permet de recharger les données
Reload.grid(row=2, column=0, columnspan=3)

Direction = Label(main, textvariable=dirsv)  # On crée un label qui affiche la direction de la carte
Direction.grid(row=3, column=0, columnspan=3)

main.after(1000, sense)
main.mainloop()
