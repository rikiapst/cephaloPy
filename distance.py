# handle a POST request
from math import radians, cos, sin, asin, sqrt
from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/test", methods=["POST"])
def distance():
    print(request.data)
    lst = json.loads(request.data)

    lat1 = lst["lat1"]
    lat2 = lst["lat2"]
    lon1 = lst["lon1"]
    lon2 = lst["lon2"]

    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    r = 6371

    result = {"result": c * r}

    return result
