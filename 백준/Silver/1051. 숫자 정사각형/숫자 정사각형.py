import sys, math
input=sys.stdin.readline

N,M=map(int,input().split())
number=[[0 for _ in range(M+1)]] + [[0] for _ in range(N)]
for _ in range(1,N+1):
    temp=str(input())
    for i in range(M):
        number[_].append(int(temp[i]))
res=1

def find_square(size):
    for i in range(1,N-size+2): #size=2, i is 1~2
        for j in range(1,M-size+2): #size=2, j is 1~4
            if number[i][j]==number[i+size-1][j]==number[i][j+size-1]==number[i+size-1][j+size-1]:
                return size*size
    return 1

for i in range(1,min(N,M)+1):
    res=max(res,find_square(i))
print(res)