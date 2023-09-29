'''
n=int(input())
k=0
for i in str(n):
    k=k+int(i)
print(k)
    '''

n=int(input())
temp=n;
sum=0;
for i in range(1,n,n//10):
    sum=sum+int(temp%10)
    temp=temp//10
print(sum)
    
    
    