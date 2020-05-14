# Uses python3
import sys
def optimal_weight(w,n,weight):
    value=[[0 for j in range(n+1)] for i in range(w+1)]
    for i in range(1,n+1):
        value[0][i]=0
    for j in range(1,w+1):
        value[j][0]=0
    val=0
    for i in range(1,n+1):
        for j in range(1,w+1):
            value[j][i]=value[j][i-1]
            if weight[i-1]<=j:
                val=value[j-weight[i-1]][i-1]+weight[i-1]
                if value[j][i]<val:
                    value[j][i]=val
    return value[w][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    w, n, *weight = list(map(int, input.split()))
    print(optimal_weight(w,n,weight))