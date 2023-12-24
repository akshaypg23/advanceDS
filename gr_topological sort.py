def topoSort(self, V, adj):
        # Code here
        degree=[0]*V
        visited=[0]*V
        
        for i in range(V):
            for neb in adj[i]:
                degree[neb]+=1
        
        q=[]
        for i in range(V):
            if degree[i] == 0:
                q.append(i)
        count=0
        ans=[]
        while(q!=[]):
            node= q.pop(0)
            visited[node]=1
            ans.append(node)
            for neb in adj[node]:
                if not visited[neb]:
                    degree[neb]-=1
                    if degree[neb]==0:
                        q.append(neb)
                    
        return ans
