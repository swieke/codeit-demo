import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def sweep():
    data = request.get_json();
    logging.info("data received: {}".format(data))

    # Parse data
    tests = data["tests"]
    res = {}

    for key, value in tests.items():
        count = 0
        floor = value['floor']
        print(floor)

        for i in range(len(floor)):
            if (floor[i] > 0):
                count += floor[i]
            elif (i > 0 and floor[i] == 0):
                count += 1

        res[key] = {
            count
        }

    ans = {
        "answers" : res
    }
    
    return json.dumps(ans)

