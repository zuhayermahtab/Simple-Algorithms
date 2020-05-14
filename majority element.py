# Uses python3
import sys
def get_majority_element(a):
    n=len(a)
    if n==1:
        return a[0]
    elif n==0:
        return None
    m=n//2
    x=get_majority_element(a[:m])
    y=get_majority_element(a[m+1:])
    if x==y:
        return x
    c1=a.count(x)
    c2=a.count(y)
    if c1>m:
        return x
    elif c2>m:
        return y
    else:
        return None
    

if __name__ == '__main__':
    input = "10 2 12 2 56 2 2 2 2 54 5"
    n, *a = list(map(int, input.split()))
    if get_majority_element(a)!=None:
        print(1)
    else:
        print(0)
    print(get_majority_element(a))
 

