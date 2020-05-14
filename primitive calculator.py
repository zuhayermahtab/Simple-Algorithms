#python3
import sys
import math
def calculator(n):
    minoperation=[math.inf]*(n+1)
    ops=[0]*(n+1)
    minoperation[0]=0
    minoperation[1]=0
    for i in range(2,n+1):
        numop1=math.inf
        numop2=math.inf
        if i%3==0:
            numop1=minoperation[i//3]+1
        elif i%2==0:
            numop2=minoperation[i//2]+1
        numop3=minoperation[i-1]+1
        x=min(numop1,numop2,numop3)
        minoperation[i]=x
        if numop1==x:
            ops[i]=3
        elif numop2==x:
            ops[i]=2
        elif numop3==x:
            ops[i]=1
    y=n
    while y>=1:
        sequence.append(y)
        if ops[y]==3 or ops[y]==2:
            y=y//ops[y]
        else:
            y-=1
    return sequence
sequence=[]
input = sys.stdin.read()
n = int(input)
sequence = calculator(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

    
    
    
    
