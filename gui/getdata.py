from datetime import datetime
from collections import OrderedDict


data = OrderedDict()
data["Time"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
data["Temperature"] = "19.94"
data["Pressure"] = "1012.97"
data["Humidity"] = "43.83"

get = [data["Time"], data["Temperature"], data["Pressure"], data["Humidity"]]
# print(get)
[print(item) for item in get]
