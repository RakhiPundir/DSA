class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])
        seen = set()
        
        def dfs(r, c):
            nonlocal perimeter
            if ((r, c) in seen):
                return
            if (r < 0 or r >= m) or (c < 0 or c >= n) \
            or (grid[r][c] == 0):
                perimeter += 1
                return
            
            seen.add((r, c))
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r, c - 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
                    
        return perimeter
