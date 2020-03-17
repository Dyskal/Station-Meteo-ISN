from sense_emu import SenseHat
from datetime import datetime
from collections import OrderedDict

sense = SenseHat()

data = OrderedDict()

data["Time"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
data["Température"] = round(sense.temp, 2)
data["Pression"] = round(sense.pressure, 2)
data["Humidité"] = round(sense.humidity, 2)

print(data["Time"])
print(data["Température"])
print(data["Pression"])
print(data["Humidité"])
