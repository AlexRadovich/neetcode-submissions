class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ret = []

        row,col = 0,0

        state = 0

        while 1:
            print(row,col)
            if matrix[row][col] != -101:
                ret.append(matrix[row][col])
            matrix[row][col] = -101

            if state == 0:
                temp = [row,col +1]
            if state == 1:
                temp = [row +1,col]
            if state == 2:
                temp = [row,col -1]
            if state == 3:
                temp = [row-1,col]

            if 0 <= temp[0] < len(matrix) and 0<= temp[1] < len(matrix[0])   and matrix[temp[0]][temp[1]] != -101:
                row,col = temp[0],temp[1]
            else:
                state = (state + 1) % 4

            if len(ret) == len(matrix[0]) * len(matrix):
                break

        return ret

            