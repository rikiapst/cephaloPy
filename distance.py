# handle a POST request
from math import radians, cos, sin, asin, sqrt
from flask import Flask
import json
app = Flask(__name__)

data = [{
    "lat1": 53.32055555555556,
    "lat2": 53.31861111111111,
    "lon1": -1.7297222222222221,
    "lon2": -1.6997222222222223
}]

coordinates = json.dumps(data)


@app.route("/test", methods=["POST"])
def distance(json_value):
    lst = json.loads(json_value)

    lat1 = lst[0]["lat1"]
    lat2 = lst[0]["lat2"]
    lon1 = lst[0]["lon1"]
    lon2 = lst[0]["lon2"]

    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    r = 6371

    return (c * r)


newList = distance(coordinates)
print(coordinates)
print(newList, 'K.M')
