class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>len(matrix) or j>len(matrix[0]):
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            
            l=1
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                if x+i<len(matrix) and y+j<len(matrix[0]) and matrix[i][j]>matrix[x+i][y+j]:
                    l=max(l,1+dfs(x+i,y+j))
            dp[i][j]=l
            return dp[i][j]

        
        ans=float('-inf')
        dp=[[-1 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans=max(ans,dfs(i,j))
        return ans