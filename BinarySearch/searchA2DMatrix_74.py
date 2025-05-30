class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        colsize = len(matrix)
        rowsize = len(matrix[0])

        l = 0
        u = colsize - 1

        while l <= u:
            m = (l + u) // 2
            row = matrix[m]
            if (target < row[0]):
                u = m - 1
            elif (target > row[rowsize - 1]):
                l = m + 1
            else:
                l_inner = 0
                u_inner = rowsize - 1

                while l_inner <= u_inner:
                    m_inner = (l_inner + u_inner) // 2

                    if target == row[m_inner]:
                        return True 
                    elif target < row[m_inner]:
                        u_inner = m_inner - 1
                    else:
                        l_inner = m_inner + 1
                
                break
        return False
        

