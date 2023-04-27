# Recursive way

class Solution1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        def fun(i,j):
            if i>=len(matrix) or j>=len(matrix[0]) or j<0:
                return float('inf')
            
            if i==len(matrix)-1:
                return matrix[i][j]
            
            return matrix[i][j]+min(fun(i+1,j-1),fun(i+1,j),fun(i+1,j+1))

        
        ans=float('inf')
        for idx in range(len(matrix[0])):
            v=fun(0,idx)
            ans=min(ans,v)

        return ans




# DP way 

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        def fun(i,j):
            
            if i>=len(matrix) or j>=len(matrix[0]) or j<0:
                return float('inf')
            
            if dp[i][j]!=-float('inf'):
                return dp[i][j]

            if i==len(matrix)-1:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = matrix[i][j]+min(fun(i+1,j-1),fun(i+1,j),fun(i+1,j+1))
    
            return dp[i][j]


        dp=[[-float('inf') for i in range(len(matrix))] for j in range(len(matrix[0]))]
        ans=float('inf')
        for idx in range(len(matrix[0])):
            dp[0][idx]=fun(0,idx)
            ans=min(ans,dp[0][idx])

        return ans

