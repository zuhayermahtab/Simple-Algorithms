#python3
import sys
import random
def partition(a,l,r):
    x=a[l]
    j=l
    j2=r
    count=0
    i=l+1
    while i<=j2:
        if a[i]<=x:
            j=j+1
            a[i],a[j]=a[j],a[i]
            i+=1
        elif a[i]>x:
            a[i],a[j2]=a[j2],a[i]
            j2-=1
        else:
            i+=1
            
    a[l],a[j]=a[j],a[l]
    return j,j2

def quicksort(a,l,r):
    if l>=r:
        return
    k=random.randint(l,r)
    a[k],a[l]=a[l],a[k]
    m1,m2=partition(a,l,r)
    quicksort(a,l,m1-1)
    quicksort(a,m2+1,r)
    return a
    
if __name__ == '__main__':
    input = "5 2 3 9 2 9"
    n, *a = list(map(int, input.split()))
    quicksort(a, 0, n-1)
    for x in a:
        print(x, end=' ')

