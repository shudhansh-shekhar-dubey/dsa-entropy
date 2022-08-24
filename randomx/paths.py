from collections import deque


class Point:
    def __init__(self, c, r):
        self.c = c
        self.r = r


class Solution:
    def uniquePathsWithObstacles(self, grid) -> int:
        path = deque()
        count = 0

        cols = len(grid[0])
        rows = len(grid)

        path.append(Point(0, 0))

        while path:
            point = path.popleft()

            if grid[point.r][point.c] == 0:
                if point.c == cols - 1 and point.r == rows - 1:
                    count = count + 1

                if point.c + 1 < cols and grid[point.r][point.c + 1] == 0:
                    path.append(Point(point.c + 1, point.r))

                if point.r + 1 < rows and grid[point.r + 1][point.c] == 0:
                    path.append(Point(point.c, point.r + 1))

        return count

    def uniquePathsWithObstacles2(self, grid) -> int:
        cols = len(grid[0])
        rows = len(grid)
        temp = [[0 for i in range(cols)] for j in range(rows)]

        if grid[0][0] == 1:
            return 0

        temp[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1: # if not 1
                    if c - 1 >= 0 and grid[r][c-1] != 1:  # if left exists but not 1
                        temp[r][c] = temp[r][c] + temp[r][
                            c - 1]  # update current value
    
                    if r - 1 >= 0 and grid[r-1][c] != 1:  # if up exists but not 1
                        temp[r][c] = temp[r][c] + temp[r - 1][
                            c]  # update current value

        return temp[rows - 1][cols - 1]
