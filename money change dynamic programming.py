#python3
import math
import sys
def dpchange(money):
    coins=[1,3,4]
    mincoin=[0]*(money+1)
    for m in range(1,money+1):
        mincoin[m]=math.inf
        for i in coins:
            if m>=i:
                numcoin=mincoin[m-i]+1
                if numcoin<=mincoin[m]:
                    mincoin[m]=numcoin
    return mincoin[money]

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(dpchange(money))