class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res=0
        for i in range(len(mat)):
            res+=mat[i][i]
            mat[i][i]=-1
        
        n=len(mat)-1
        for i in range(len(mat)):
            # print(mat[i][n-i])
            if mat[i][n-i]!=-1:
                res+=mat[i][n-i]
        return res