from collections import deque
import sys

def BFS(G):
    visited = [0 for _ in range(V+1)]
    
    for i in range(1,V+1):
        if visited[i]==0:
            q = deque([i])
            visited[i]=1

            while q:  
                node = q.popleft()
                
                nodeTeam = visited[node]
                nextTeam = nodeTeam*-1
                for next in G[node]:
                    if visited[next]==0:
                        visited[next] = nextTeam
                        q.append(next)
                                
                    elif visited[next] == nodeTeam:
                        return 'NO'
    return 'YES'

T = int(sys.stdin.readline())
for _ in range(T):
    answer='YES'
    
    V,E = map(int,sys.stdin.readline().split())
    G = [ [] for _ in range(V+1)]

    for i in range(E):
        u,v = map(int, sys.stdin.readline().split())
        G[u].append(v)
        G[v].append(u)
        
    answer = BFS(G)
    print(answer)