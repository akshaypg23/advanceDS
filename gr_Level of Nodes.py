class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        q=[]
        visited=[0]*V
        
        start=(0,0)
        visited[0]=1
        q.append(start)
        while(q!=[]):
            node,level = q.pop(0)
            if node==X:
                return level
            for neb in adj[node]:
                if not visited[neb]:
                    visited[neb]=1
                    q.append((neb,level+1))            
        return -1
