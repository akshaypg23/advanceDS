class Solution:
	def isBipartite(self, V, adj):
		#code here
        q=[]
        start=0;
        q.append(start)
        colored=[-1]*V
        colored[start]=0
        
        while(q!=[]):
            node=q.pop(0)
            
            for neb in adj[node]:
                if colored[neb]!=-1:
                    colored[neb]= not colored[node]
                
                if colored[neb] == colored[node]:
                    return False
        
        return True
