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
    sumOfDaysDuration = sum(days)
    i = 0
    totalDuration = 0
    booksRead = 0

    while (i < len(books)):
        if (totalDuration + books[i] <= sumOfDaysDuration):
            totalDuration += books[i]
            booksRead += 1
        i += 1

    return json.dumps({
        "optimalNumberOfBooks" : booksRead
    })