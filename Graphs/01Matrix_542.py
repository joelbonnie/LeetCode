class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
                else:
                    queue.append((i,j))
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        while queue: 
            i, j = queue.popleft()
            dist = mat[i][j]

            for ver, hor in directions: 
                new_i, new_j = (i + ver, j + hor)

                if 0 <= new_i < m and 0 <= new_j < n: 
                    currDist = mat[new_i][new_j]
                    if currDist > dist + 1:
                        mat[new_i][new_j] = dist + 1 
                        queue.append((new_i, new_j))
        
        return mat

