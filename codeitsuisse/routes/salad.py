import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def checkSalad():
    data = request.get_json();
    logging.info("data received: {}".format(data))

    # Parse data
    n = data.get("number_of_salads");
    s = data.get("salad_prices_street_map")

    sumArr = 0
    numSalad = 0

    for arr in s:
        i = 0
        maxSum = 0;

        while(i < len(arr) - n):
            sum = 0
            numOfShop = 0
            for i in range(n):
                if (arr[i] != 'X'):
                    numOfShop += 1
                    sum += int(arr[i])
            
            if (sum > maxSum and numOfShop == n): 
                maxSum = sum
                
        numSalad = maxSum

    res = {
        "result" : numSalad
    }

    return json.dumps(res)