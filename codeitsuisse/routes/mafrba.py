import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

# { "maApple": 1, "maWatermelon": 2, "maBanana": 3 }

@app.route('/fruitbasket', methods=['POST'])
def predictFruit():
    data = str(request.get_data())
    logging.info("data received: {}".format(data))
    print(data)

    parseIndexList = [i+1 for i in range(len(data)) if data[i] == ':']

    numOfFruitA = int(data[parseIndexList[0]:parseIndexList[0]+2])
    numOfFruitB = int(data[parseIndexList[1]:parseIndexList[1]+2])
    numOfFruitC = int(data[parseIndexList[2]:parseIndexList[2]+2])

    print(numOfFruitA)
    print(numOfFruitB)
    print(numOfFruitC)

    prediction = numOfFruitA * 55 + numOfFruitB * 55 + numOfFruitC * 50
    return("{}".format(prediction))
