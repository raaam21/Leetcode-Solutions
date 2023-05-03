class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m=len(matrix)
        n=len(matrix[0])
        self.ps=[[0 for j in range(n)] for i in range(m)]
        self.ps[0][0]=matrix[0][0]

        for j in range(1,n):
            self.ps[0][j]=self.ps[0][j-1]+matrix[0][j]

        for i in range(1,m):
            self.ps[i][0]=self.ps[i-1][0]+matrix[i][0]

        for i in range(1,m):
            for j in range(1,n):
                self.ps[i][j]=self.ps[i-1][j]+self.ps[i][j-1]-self.ps[i-1][j-1]+matrix[i][j]
  
        print(self.ps)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.ps[row2][col2]
        
        if row1>0:
            ans-=self.ps[row1-1][col2]
        if col1>0:
            ans-=self.ps[row2][col1-1]
        if row1>0 and col1>0:
            ans+=self.ps[row1-1][col1-1]

        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
