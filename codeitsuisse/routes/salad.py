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

    # base case check
    if (n > len(s[0]) or n > 100 or len(s[0]) > 100):
        return json.dumps({"result" : 0})

    sumArr = 0
    numSalad = 0

    for arr in s:
        i = 0
        maxSum = 0;

        while(i < len(arr) - n):
            sum = 0
            numOfShop = 0
            for j in range(n):
                if (arr[i + j] != 'X'):
                    numOfShop += 1
                    sum += int(arr[i + j])
                    # print(numOfShop)
                    
            print("SUM: {}".format(sum))
            print("NUMOFSHOP: {}".format(numOfShop))
            
            if (sum > maxSum and numOfShop == n): 
                maxSum = sum
                if (maxSum > numSalad): numSalad = maxSum

            i += 1;

    res = {
        "result" : numSalad
    }

    return json.dumps(res)