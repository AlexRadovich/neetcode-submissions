class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = 0
        flag = False
        path = set()

        def dfs(i,j, board, cur, word):
            if cur == len(word):
                flag = True
                return True
            if cur > len(word):
                return False
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return False
            if (i,j) in path:
                return False
            if word[cur] != board[i][j]:
                return False
            
            cur += 1
            path.add((i,j))

            k = dfs(i+1,j,board, cur, word) or dfs(i-1,j,board, cur, word) or dfs(i,j+1,board, cur, word) or dfs(i,j-1,board, cur, word) 
            if((i,j) in path): path.remove((i,j))     
            return k


        for i in range(len(board)):
            for j in range(len(board[0])):
                     
                if dfs(i,j,board,0, word):
                    return True

        return flag

            