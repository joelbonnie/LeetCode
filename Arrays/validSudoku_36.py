class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMap = defaultdict(set)
        columnMap = defaultdict(set)
        squareMap = defaultdict(set)

        for row in range(0,9,1):
            for col in range(0,9,1):

                currentElement = board[row][col]

                if currentElement == '.':
                    continue

                if ((currentElement in rowMap[row]) or 
                    (currentElement in columnMap[col]) or 
                    (currentElement in squareMap[(row // 3, col // 3)])):
                    return False 


                rowMap[row].add(currentElement)
                columnMap[col].add(currentElement)
                squareMap[(row // 3, col // 3)].add(currentElement)



        return True
        
