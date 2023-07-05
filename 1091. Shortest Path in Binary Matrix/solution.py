class Solution:
    # Takes in an n by n binary matrix and returns the length of the
    # shortest path from the top-left corner to the bottom-right corner
    # using BFS. It returns -1 if no path has been found. All visited
    # cells have to be 0s and the adjacent cells are connected 
    # diagonally as well as horizontally and vertically.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # print(grid)

        # if either the top-left corner or bottom-right corner are
        # not clear, that means it's impossible to find a clear path
        # between the two corners
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # create the queue that stores the next coordinates to visit
        queue = [[0, 0]]

        # the number of times the outer loop has iterated, or the
        # number of cells visited/round num. Starts at 1
        roundNum = 1

        # while the queue isn't empty, process nodes for BFS traversal:
        while queue:
            # measure the queue's length and iterate that many times
            queueLen = len(queue)

            for i in range(queueLen):
                # pop off the front of the queue and save the indices
                indices = queue.pop(0)
                # print("indices:", indices)
                x = indices[0]
                y = indices[1]

                # if we're at the end, we can return the round number, assuming that
                # the width of grid is the same as thje height of grid
                if indices[0] == len(grid) - 1 and indices[1] == len(grid) - 1:
                    return roundNum

                # check for zeroes in all 8 directions and add to queue if needed
                if x-1 >= 0 and y-1 >= 0 and grid[x-1][y-1] == 0:
                    queue.append([x-1, y-1])
                    grid[x-1][y-1] = -1
                
                if y-1 >= 0 and grid[x][y-1] == 0:
                    queue.append([x, y-1])
                    grid[x][y-1] = -1
                
                if x+1 < len(grid) and y-1 >= 0 and grid[x+1][y-1] == 0:
                    queue.append([x+1, y-1])
                    grid[x+1][y-1] = -1
                
                if x-1 >= 0 and grid[x-1][y] == 0:
                    queue.append([x-1, y])
                    grid[x-1][y] = -1
                
                if x+1 < len(grid) and grid[x+1][y] == 0:
                    queue.append([x+1, y])
                    grid[x+1][y] = -1
                
                if x-1 >= 0 and y+1 < len(grid) and grid[x-1][y+1] == 0:
                    queue.append([x-1, y+1])
                    grid[x-1][y+1] = -1
                
                if y+1 < len(grid) and grid[x][y+1] == 0:
                    queue.append([x, y+1])
                    grid[x][y+1] = -1
                
                if x+1 < len(grid) and y+1 < len(grid) and grid[x+1][y+1] == 0:
                    queue.append([x+1, y+1])
                    grid[x+1][y+1] = -1
            
            roundNum += 1


        # if we could never find a clear path, return -1
        return -1
