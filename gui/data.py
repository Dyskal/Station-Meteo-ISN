from datetime import datetime
from collections import OrderedDict
# from sense_hat import SenseHat


def getData():
    """Fonction permettant de récuperer les données météo de la carte"""
    # sense = SenseHat()
    data = OrderedDict()

    data["Time"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    # data["Temperature"] = round(sense.temp, 2)
    # data["Pressure"] = round(sense.pressure, 2)
    # data["Humidity"] = round(sense.humidity, 2)

    data["Temperature"] = "19.94"
    data["Pressure"] = "1012.97"
    data["Humidity"] = "43.83"

    return data


if __name__ == '__main__':
    weather = getData()
    stats = [weather["Time"], weather["Temperature"], weather["Pressure"], weather["Humidity"]]
    [print(item) for item in stats]
