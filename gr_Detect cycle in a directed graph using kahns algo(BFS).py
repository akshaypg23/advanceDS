class Solution:
    #Function to detect cycle in an undirected graph.
	def isCyclic(self, V: int, adj) -> bool:
	    degree=[0]*V
        visited=[0]*V
        #indegree
        for i in range(V):
            for neb in adj[i]:
                degree[neb]+=1
        
        q=[]
        for i in range(V):
            if degree[i] == 0:
                q.append(i)
        
        count=0
        
        while(q!=[]):
            node= q.pop(0)
            visited[node]=1
            count+=1
            for neb in adj[node]:
                if not visited[neb]:
                    degree[neb]-=1
                    if degree[neb]==0:
                        q.append(neb)
        
        if count==V:
            return False
        else:
            return True
