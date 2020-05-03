#python 3
import sys

def gcd_euclid(a, b):
    if b==0:
        return a
    else:
        x=a%b
        return gcd_euclid(b,x)
def lcm(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a*b/gcd_euclid(a,b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
