import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def findCluster():

    data = request.get_json();
    print(data)
    print(type(data))
    logging.info("data received: {}".format(data))

    grid = data
    visited = []

    def dfs(grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '*' or [i, j] in visited:
            return
    
        grid[i][j] = '1'
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
        
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                visited.append([i, j])
                dfs(grid, i, j)
                count += 1

    return json.dumps({ "answer" : count })

