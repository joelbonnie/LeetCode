class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        searchQueue = deque()

        freshCount = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    searchQueue.append((i,j))

        if freshCount == 0: 
            return 0
        
        timeCounter = 0 

        searchDirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while searchQueue: 
            timeCounter += 1

            # Check each level at a time2
            for cell in range(len(searchQueue)): 
                x,y = searchQueue.popleft()
                if grid[x][y] == 2: 
                    for dx, dy in searchDirs:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < m and 0 <= new_y < n: 
                            if grid[new_x][new_y] == 1: 
                                grid[new_x][new_y] = 2
                                freshCount -= 1
                                if freshCount == 0: 
                                    return timeCounter 
                                searchQueue.append((new_x, new_y))

        
        if freshCount != 0: 
            return -1 

        

