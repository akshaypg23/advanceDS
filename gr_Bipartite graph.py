class Solution:
	def BFS(self,node,adj):
        q=[]
        q.append(node)
        self.colored[node]=0
        while(q!=[]):
            node= q.pop(0)
            # if node in adj[node]:
            #     return False;
            for neb in adj[node]:
                if self.colored[neb]==-1:
                    self.colored[neb]= 1 - self.colored[node]
                    q.append(neb)
                elif self.colored[neb] == self.colored[node]:
                    return False
        return True
        
	def isBipartite(self, V, adj):
		V=len(adj)
        self.colored =[-1]*V
        for i in range(V):
            if self.colored[i]==-1:
                if self.BFS(i,adj) == False:
                    return False
        return True
