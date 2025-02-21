from collections import deque
import sys

def solve(xqueue,xstring):
    count=0
    for index in xstring:
        if index=='R':
            count+=1
        elif index=='D':
            if len(xqueue)==0:
                return "error"
            else:
                if count%2==0:
                    xqueue.popleft()
                elif count%2==1:
                    xqueue.pop()
    if count%2==1:
        xqueue.reverse()
    res="["
    if len(xqueue)!=0:
        for i in xqueue:
            res+=str(i)
            res+=','
        res=res[:-1]
    res+=']'
    return res


num=int(sys.stdin.readline())
charcters="[],"

for i in range(num):
    num_list=[]
    function=str(sys.stdin.readline())
    length=int(sys.stdin.readline())
    temp=sys.stdin.readline()
    if length==0:
        num_list=[]
    else:
        temp=temp[1:-2]
        num_list=temp.split(',')
        for i in range(len(num_list)):
            num_list[i]=int(num_list[i])

    queue=deque(num_list)
    print(solve(queue,function))
