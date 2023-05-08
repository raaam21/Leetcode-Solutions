class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # we'll change the value of grid to 2 to keep track of visited
        # initializing a queue to keep track of adjacnt nodes:
        qu=[]

        # adding multiple sources to BFS queue
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    qu.append([i,j])
                    grid[i][j]=2
        
        # if queue contains all the lands that means no other water cell is present in the grid
        if len(qu)==len(grid)*len(grid[0]):
            return -1
        


        k=0
        
        # simple nfs condition pop till empty
        while(len(qu)>0):
            
            # traversing for that particular level only
            r=len(qu)
            for m in range(r):
                i,j=qu.pop(0)
                if i-1>=0 and grid[i-1][j]==0:
                    qu.append([i-1,j])
                    grid[i-1][j]=2
                
                if j-1>=0 and grid[i][j-1]==0:
                    qu.append([i,j-1])
                    grid[i][j-1]=2

                if i+1<len(grid) and grid[i+1][j]==0:
                    qu.append([i+1,j])
                    grid[i+1][j]=2

                if j+1<len(grid[0]) and grid[i][j+1]==0:
                    qu.append([i,j+1])
                    grid[i][j+1]=2
            
            k+=1

        # k will be increased  for the last level so deccrement

        return k-1