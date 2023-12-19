def detectCycle(slef,i,visited):
        parent=-1;source=i
		q=[(source,parent)]
		visited[0]=1
        while(q!=[]):
            node,parent = q.pop(0)
            for neb in adj[node]:
                # print(neb,node)
                if neb!=parent:
                    if visited[neb]==1:
                        return True
                    else:
                        visited[neb]=1
                        q.append((neb,node))
                        # print(q)
        return False
        
#Function to detect cycle in an undirected graph.
def isCycle(self, V: int, adj: List[List[int]]) -> bool:
    visited=[0]*V
for i in range(V):
    if visited[i]!=1:
        if self.detectCycle(i,visited)==True:
            return True
return False
