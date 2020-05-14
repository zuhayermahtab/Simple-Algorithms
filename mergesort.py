#python3
import sys

def mergesort(a,l,r):
    if l>=r:
        return a[l:r+1]
    m=(l+r)//2
    b=mergesort(a,l,m)
    c=mergesort(a,m+1,r)
    a=merge(b,c)
    return a
def merge(b,c):
    d=[]
    while len(b)!=0 and len(c)!=0:
        B=b[0]
        C=c[0]
        if B<=C:
            d.append(B)
            b.remove(B)
        else:
            d.append(C)
            c.remove(C)
    d.extend(c)
    d.extend(b)
    return d
        
if __name__ == '__main__':
    input = "10 10 9 8 7 6 5 4 3 2 1"
    n, *a = list(map(int, input.split()))
    x=mergesort(a,0,n)
    print(x)