class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        top = False
        left = False
        
        for i in matrix[0]:
            if i == 0:
                top = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                left = True
                break
        

        

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        
        for x in matrix:
            print(x)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    continue
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        for x in matrix:
            print(x)

        if top:
            matrix[0] = [0] * len(matrix[0])

        if left:
            for i in range(len(matrix)):
                matrix[i][0] = 0 
