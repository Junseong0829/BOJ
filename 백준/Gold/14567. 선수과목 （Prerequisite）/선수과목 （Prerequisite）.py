import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
x=[[] for _ in range(N+1)]
indegree=[0]*(N+1)
res=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    indegree[b]+=1
    x[a].append(b)

def topologySort():
    queue=deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            queue.append((i,1))
    while queue:
        temp,cnt=queue.popleft()
        res[temp]=cnt
        for j in x[temp]:
            indegree[j]-=1
            if indegree[j]==0:
                queue.append((j,cnt+1))
            
topologySort()
for element in res[1:]:
    print(element,end=" ")