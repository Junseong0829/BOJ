"""
f(3)=f(1)+f(2), 
f(2)=f(1)+f(0)

f(3)=f(0)+2f(1)  -> 3 = 1 2

(1,0) (0,1) (1,1) (1,2)
  0     1     2     3

"""
dp=[(0,0)]*41
dp[0],dp[1]=(1,0),(0,1)
for i in range(2,41):
    a=dp[i-1][0]+dp[i-2][0]
    b=dp[i-1][1]+dp[i-2][1]
    dp[i]=(a,b)
num=int(input())
for i in range(num):
    temp=int(input())
    print(dp[temp][0],end=" ")
    print(dp[temp][1])