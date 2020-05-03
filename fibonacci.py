#python 3
n=int(input())
f=[]*n
for i in range(0,n+1):
    f.append(i)
for i in range(2,n+1):
    f[i]=(f[i-2]+f[i-1])%10
print(f[n])
    
    