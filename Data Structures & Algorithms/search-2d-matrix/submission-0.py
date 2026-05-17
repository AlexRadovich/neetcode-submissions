class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        
        l = 0
        r = rows * cols - 1
        m = 0



        if matrix[0][0] == target: return True
        if matrix[rows-1][cols-1] == target: return True

        while matrix[m // cols][m % cols] != target:

            m = (l+r)//2

            if matrix[m // cols][m % cols] < target:
                if l == m:
                    return False
                l = m
            else:
                if r == m:
                    return False
                r = m

        return True


