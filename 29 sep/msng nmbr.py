'''
n=list(map(int,input().split(" ")))
s=[]
for i in range(max(n)+1):
    print(i)
    if i>=0 and i not in n:
        s.append(i)
print(s[0])

n=list(map(int,input().split(" ")))
for i in range(max(n) + 1):  
    found = False
    for item in n:
        if i == item:
            found = True
            break
    if not found:
        print(i)
'''

def findnum(arr,n):
    if(n==0):
        return 1
    i=0
    while i<n:
        if arr[i]>=0 and arr[i] <= n and arr[i]!=arr[arr[i]-1]:
            temp=arr[i]-1
            temp2=arr[i]
            arr[i]=arr[temp]
            arr[temp]=temp2
        else:
            i += 1
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1
arr=[10,4,-4,1]
n=len(arr)
print(findnum(arr,n))
            

















