import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def findOptimalReading():
    data = request.get_json();
    logging.info("data received: {}".format(data))

    # Parse data
    numBooks = data.get("numberOfBooks");
    numDays = data.get("numberOfDays");
    books = data.get("books");
    days = data.get("days");

    # Initialization
    booksReadCount = 0
    books.sort(reverse=True)
    days.sort(reverse=True)

    taken = []

    for dayTime in days:
        remainingTime = dayTime
        for i in range(len(books)):
            if (books[i] <= remainingTime and i not in taken):
                booksReadCount += 1
                remainingTime -= books[i]
                taken.append(i)
                # print("Insert {} to {}, remaining {}".format(books[i], dayTime, remainingTime))

    
    res = {
        "optimalNumberOfBooks" : booksReadCount
    }
    logging.info("Result: ")
    logging.info(res)
    return json.dumps(res)