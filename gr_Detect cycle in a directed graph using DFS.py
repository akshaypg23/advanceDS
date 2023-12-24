    
    def dfsCycle(self,node):
        for neb in adj[node]:
            # print(neb,node)
            if not self.visited[neb]:
                self.visited[neb]=1
                self.pathvisited[neb]=1
                if self.dfsCycle(neb)==True:
                    return True
                # print(neb,self.visited,self.pathvisited)
                self.pathvisited[neb]=0
            if self.visited[neb]==1 and self.pathvisited[neb]==1:
                return True
        return False
        
        
    #Function to detect cycle in an undirected graph.
	def isCyclic(self, V: int, adj) -> bool:
	    self.visited=[0]*V
        self.pathvisited=[0]*V
        
        for i in range(V):
            if not self.visited[i]:
                if self.dfsCycle(i)==True:
                    return True
        return False
