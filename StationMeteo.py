from random import randint
from tkinter import StringVar, PhotoImage, Canvas
from tkinter.ttk import Label, Button
from PIL import Image, ImageTk
from ttkthemes import ThemedTk, ThemedStyle
from gui.excel import updateXslx, excelwb
# from sense_hat import SenseHat

main = ThemedTk(background=True, theme="equilux")  # On crée une fenetre tkinter
images = [ImageTk.PhotoImage(Image.open("gui/resources/nord.png")),
          ImageTk.PhotoImage(Image.open("gui/resources/est.png")),
          ImageTk.PhotoImage(Image.open("gui/resources/sud.png")),
          ImageTk.PhotoImage(Image.open("gui/resources/ouest.png"))]
imgIndice = 0  # A changer
angle = 90  # On attribue manuellement un angle pour tester

# sense = SenseHat()
timeVar = StringVar()  # On définit des chaines de caractère variables pour les labels tkinter
temperatureVar = StringVar()
pressureVar = StringVar()
humidityVar = StringVar()
directionVar = StringVar()


def sense():
    """Boucle pour recevoir les appuis du joystick et la direction de la boussole de la carte"""
    # angle = sense.get_compass()
    global angle
    if angle < 45 or angle > 315:
        directionVar.set('Nord')
        compass.itemconfig(canvasImg, image=images[0])
        # sense.set_rotation(90)
    elif angle < 135:
        directionVar.set('Est')
        compass.itemconfig(canvasImg, image=images[1])
        # sense.set_rotation(0)
    elif angle < 225:
        directionVar.set('Sud')
        compass.itemconfig(canvasImg, image=images[2])
        # sense.set_rotation(270)
    else:
        directionVar.set('Ouest')
        compass.itemconfig(canvasImg, image=images[3])
        # sense.set_rotation(180)
    # sense.show_letter(dirsv.get()[0])
    angle = randint(0, 360)
    main.after(1000, sense)


def reloadData():
    """Cette fonction permet de mettre à jour les données météo"""
    from gui.data import getData
    data = getData()
    timeVar.set("Date: " + data["Time"])
    temperatureVar.set("Température: " + data["Temperature"] + " °C")
    pressureVar.set("Pression: " + data["Pressure"] + " hPa")
    humidityVar.set("Humidité: " + data["Humidity"] + " %")
    updateXslx()  # Et ensuite de mettre les valeurs dans le fichier Excel


def close():
    """Fonction pour fermer la fenetre correctement"""
    main.destroy()
    excelwb.close()


main.title('Station météo')
main.geometry('515x615')  # 350x100
main.iconphoto(True, PhotoImage(file="gui/resources/icon.png"))
style = ThemedStyle(main)
main.protocol('WM_DELETE_WINDOW', close)
reloadData()
# sense.stick.direction_any = reloadData

timeLabel = Label(main, textvariable=timeVar)  # On crée un label qui affiche la date
timeLabel.grid(row=0, column=0, columnspan=3)

temperatureLabel = Label(main, textvariable=temperatureVar)  # On crée un label qui affiche la température
temperatureLabel.grid(row=1, column=0)

pressureLabel = Label(main, textvariable=pressureVar)  # On crée un label qui affiche la pression
pressureLabel.grid(row=1, column=1)

humidityLabel = Label(main, textvariable=humidityVar)  # On crée un label qui affiche l'humidité
humidityLabel.grid(row=1, column=2)

reloadButton = Button(main, text="Recharger les données", command=reloadData)
# On crée un boutton qui permet de recharger les données
reloadButton.grid(row=2, column=0, columnspan=3)

directionLabel = Label(main, textvariable=directionVar)  # On crée un label qui affiche la direction de la carte
directionLabel.grid(row=3, column=0, columnspan=3)

compass = Canvas(main, width=450, height=450)
canvasImg = compass.create_image(0, 0, anchor='nw', image=images[imgIndice])
compass.grid(row=4, column=0, columnspan=3)

main.after(1000, sense)
main.mainloop()
