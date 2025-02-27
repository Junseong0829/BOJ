import sys
input=sys.stdin.readline

def dfs(value,visited,graph,length,target):
    global cnt
    visited[value]=True
    if value==target:
        cnt=1
        print(length)
    for i in graph[value]:
        if not visited[i]:
            dfs(i,visited,graph,length+1,target)
cnt=0
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
a,b=map(int,input().split())
m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(a,visited,graph,0,b)
if cnt==0:
    print(-1)