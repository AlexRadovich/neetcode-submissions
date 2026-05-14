class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i,j):
            if(i < 0 or i >= len(grid)): return False
            if(j < 0 or j >= len(grid[0])): return False
            if(grid[i][j] == '0'):
                return False
            
            
            grid[i][j] = '0'
            k = dfs(i+1,j),  dfs(i, j+1),  dfs(i-1 , j),  dfs(i, j-1)
            
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(dfs(i,j)):
                    count += 1
                    print(grid)
        return count
            