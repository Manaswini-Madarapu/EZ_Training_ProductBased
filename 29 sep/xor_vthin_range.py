m=int(input())
n=int(input())
xor=0
for i in range(m,n+1):
    xor=xor^i
print(xor)