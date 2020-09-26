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

    # Parse data
    # maApple = data.split('{ "maApple" : ');
    # maWatermelon = data.get("maWatermelon");
    # maBanana = data.get("maBanana");
    # print(maApple);

    # prediction = maApple * 56 + maWatermelon * 23 + maBanana * 80
    return("{}".format(150))
