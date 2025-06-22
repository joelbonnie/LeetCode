class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater), len(isWater[0])
        searchQueue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    searchQueue.append((i,j))
                else: 
                    isWater[i][j] = -1
        
        searchRadius = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while searchQueue: 
            i,j = searchQueue.popleft()

            for i_add, j_add in searchRadius:
                new_i, new_j = i + i_add, j + j_add

                if 0 <= new_i < m and 0 <= new_j < n:
                    if isWater[new_i][new_j] == -1: 
                        isWater[new_i][new_j] = isWater[i][j] + 1 
                        searchQueue.append((new_i, new_j))
            
        return isWater
