class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islandCount = 0 
        m,n = len(grid), len(grid[0])

        def dfs(ver, hor):
            if grid[ver][hor] == "1": 
                grid[ver][hor] = "0"       
                # Left 
                if hor > 0: dfs(ver, hor - 1)
                # Right 
                if hor < n - 1: dfs(ver, hor + 1)
                # Up
                if ver > 0: dfs(ver - 1, hor)
                # Down
                if ver < m - 1: dfs(ver + 1, hor)
        
        for i in range(m):
            for j in range(n):
                currentPoint = grid[i][j]
                if currentPoint == "1": 
                    self.islandCount += 1
                    dfs(i,j)
        
        return self.islandCount

        

