def dfs(self,node,ans,visited):
        for neb in adj[node]:
            if visited[neb]!=1:
                ans.append(neb)
                visited[neb]=1
                self.dfs(neb,ans,visited)
                
        return ans
            
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited=[0] * V
        visited[0] = 1
        ans=[]
        ans.append(0)
        ans = self.dfs(0,ans,visited)
        return ans
