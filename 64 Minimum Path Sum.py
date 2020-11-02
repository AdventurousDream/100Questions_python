from typing import List
def minPathSum(grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        ans[0][0] = grid[0][0]
        for i in range(1, m):  
            ans[0][i] = grid[0][i]+ans[0][i-1]
        for j in range(1, n):    
            ans[j][0] = grid[j][0]+ans[j-1][0]
        for j in range(1, n):
            for i in range(1, m):
                ans[j][i] = min(ans[j-1][i], ans[j][i-1]) + grid[j][i]
        return ans[-1][-1]