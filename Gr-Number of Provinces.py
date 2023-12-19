class Solution:
    def dfs(self,node,visited):
        visited[node]=1
        #adj is adj matrix type
        for index,val in enumerate(adj[node]):
            if val==1 and visited[index]!=1:
                self.dfs(index,visited)
                
    def numProvinces(self, adj, V):
        # print(adj)
        visited = [0] * V
        count=0
        for i in range(V):
            if visited[i]!=1:
                # print(i,"iiiiii");
                self.dfs(i,visited)
                count+=1 
        
        return count
