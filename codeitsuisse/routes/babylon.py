import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

# {
#     numberOfBooks: 5,
#     numberOfDays: 3,
#     books: [114, 111, 41, 62, 64],
#     days: [157, 136, 130]
# }

@app.route('/olympiad-of-babylon', methods=['POST'])
def findOptimalReading():
    data = request.get_json();
    logging.info("data received: {}".format(data))

    # Parse data
    numBooks = 5
    numDays = 3
    books = [114, 111, 41, 62, 64]
    days = [157, 136, 130]

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


