from Data import getData
from sense_hat import SenseHat

sense = SenseHat()

while True:
    events = sense.stick.get_events()
    for event in events:
        if event.action != "relased":  # or exec every x time
            getData()
