import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def findCluster(grid):

    data = request.data;
    logging.info("data received: {}".format(data))

    map = data

    def dfs(grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '*':
            return
        if (grid[i][j] == '0'):
            grid[i][j] = '1'

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

    if not grid:
        return 0
        
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return json.dumps({ "answer" : count })

