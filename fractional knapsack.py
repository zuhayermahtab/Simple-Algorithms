# Uses python3

def get_optimal_value(capacity, weights, values):
    vw=[0]*n
    visited=[0]*n
    v=0
    for i in range(0,n):
        vw[i]=values[i]/weights[i]
    while capacity>0:
        i=vw.index(max(vw))
        if weights[i]<=capacity and visited[i]==0:
            v+=values[i]
            capacity-=weights[i]
            vw[i]=0
            visited[i]=1
            
        else:
            v+=vw[i]*capacity
            capacity=0
        if sum(visited)==n:
            break
    return v


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
