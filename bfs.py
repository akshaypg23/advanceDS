def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
  # code here
  visited=[0] * V
  q=[];start=0
  q.append(start)
  visited[start]=1
  ans=[]
  while(q!=[]):
      node = q.pop(0)
      ans.append(node)
      for neb in adj[node]:
          if visited[neb]!=1:
              q.append(neb)
              visited[neb]=1
  return ans
