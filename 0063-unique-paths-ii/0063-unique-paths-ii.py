class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def f(i,j):
            if i<0 or i>len(grid)-1 or j>len(grid[0])-1 or j<0 or grid[i][j]==1:
                return 0

            if i==len(grid)-1 and j==len(grid[0])-1:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]
            
            a,b=0,0
            if 0<=i<len(grid) and 0<=j+1<len(grid[0]):
                a=f(i,j+1)
            
            if 0<=i+1<len(grid) and 0<=j<len(grid[0]):
                b=f(i+1,j)
            dp[i][j]=a+b
            return dp[i][j]

        s=0
        dp=[[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
        return f(0,0)  
        