def __init__(self):
        self.direction =[(0,-1),(0,1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]
        
    def marknearByLands(self, r, c,n, m):
        start=(r,c)
        q=[]
        q.append(start)
        while(q!=[]):
            r,c = q.pop(0)
            self.visited[r][c]=1
            for x,y in self.direction:
                nrow = r+x
                ncol = c+y
                if nrow <0 or ncol<0 or nrow>=n or ncol>=m or grid[nrow][ncol]==0:
                    continue
                if grid[nrow][ncol]==1 and self.visited[nrow][ncol]==0:
                    q.append((nrow,ncol))
                    self.visited[nrow][ncol]=1
         
    def numIslands(self,grid):
        #code here
        row=len(grid)
        col=len(grid[0])
        self.visited=[[0 for _ in range(col)] for _ in range(row)]
        count=0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and self.visited[i][j]==0:
                    self.marknearByLands(i,j,row,col)
                    count+=1
        return count
