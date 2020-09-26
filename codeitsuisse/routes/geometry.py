import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def intersection(L1, L2):
        D  = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x,y
        else:
            return False

def line(p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        return A, B, -C

@app.route('/revisitgeometry', methods=['POST'])
def getIntersection():
    data = request.get_json();
    logging.info("data received: {}".format(data))

    # Parse data
    shapeCoordinates = data.get("shapeCoordinates");
    lineCoordinates = data.get("lineCoordinates")
 
    line1 = line([lineCoordinates[0]["x"], lineCoordinates[0]["y"]], [lineCoordinates[1]["x"], lineCoordinates[1]["y"]])

    intersections = []

    for i in range(len(shapeCoordinates) - 1):
        for j in range(i + 1, len(shapeCoordinates)):
            #shapeline
            line2 = line([shapeCoordinates[i]["x"], shapeCoordinates[i]["y"]],[shapeCoordinates[j]["x"], shapeCoordinates[j]["y"]])
            result = intersection(line1, line2)
            
            if (result):
                coordinate = [round(result[0], 2), round(result[1], 2)]
                intersections.append({"x" : coordinate[0], "y" : coordinate[1]})

    
    return json.dumps(intersections)