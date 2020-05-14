#python3
import sys

def mergesort(a,l,r):
    if l>=r:
        return a[l:r+1]
    m=(l+r)//2
    b=mergesort(a,l,m)
    c=mergesort(a,m+1,r)
    a=merge(b,c,l,m,r)
    return a
def merge(b,c,l,m,r):
    d=[]
    while len(b)!=0 and len(c)!=0:
        B=b[0]
        C=c[0]
        if B<=C:
            d.append(B)
            b.pop(0)
            l+=1
        else:
            inv.append(m-l+1)
            d.append(C)
            c.pop(0)
    d.extend(c)
    d.extend(b)
    return d
        
if __name__ == '__main__':
    input = "6 9 8 7 3 2 1"
    n, *a = list(map(int, input.split()))
    inv=[]
    x=mergesort(a,0,n)
    print(sum(inv))