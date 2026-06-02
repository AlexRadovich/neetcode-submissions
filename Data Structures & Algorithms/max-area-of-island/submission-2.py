class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(grid,row,col):
            if grid[row][col] == 0: return 0
            print(row,col)

            grid[row][col] = 0

            count = 0

            if col > 0:
                count += dfs(grid,row,col-1)
            if col < len(grid[0])-1:
                count += dfs(grid,row,col+1)
            if row > 0:
                count += dfs(grid,row-1,col)
            if row < len(grid)-1:
                count += dfs(grid,row+1,col)

            return 1 + count

        best = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    print("ixs",row,col)
                    best = max(best,dfs(grid,row,col))

        return best
            
                

