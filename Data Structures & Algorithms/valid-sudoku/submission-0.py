from math import floor
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cols = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        boxes = [set(),set(),set(),set(),set(),set(),set(),set(),set()]

        brd = [["." for i in range(9)] for j in range(9)]

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                print(item)

                if item == ".":
                    continue
                if item in rows[row] or item in cols[col] or item in boxes[(col//3) + 3 * (row//3)]:
                    return False
                else:
                    rows[row].add(item) 
                    cols[col].add(item) 
                    boxes[(col//3) + 3 * (row//3)].add(item)
                    brd[((col//3) + 3 * (row//3))//3][(col//3) + 3 * (row//3) % 3] = item
                for i in range(9):

                    print(brd[i])
                print()
        return True
