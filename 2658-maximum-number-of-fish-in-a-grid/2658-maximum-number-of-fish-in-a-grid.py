class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1:
                return 0
            
            temp=grid[i][j]
            grid[i][j]=0


            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                if 0<=i+x<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j]!=0:
                    temp+=dfs(x+i,y+j)
            return temp                    

        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    a=dfs(i,j)
                    ans=max(ans,a)
        return ans