
n=list(map(int,input().split(",")))
print("after sorting")
for i in range(len(n)):
    min=n[i]
    pos=i
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            min=n[j]
            pos=j
        else:
            min=min
    n[pos]=n[i]
    n[i]=min
    print(n[i],end=" ")

print('\n')
arr=list(map(int,input().split(",")))
print("After sorting")
for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
    print(arr[i],end=" ")
            

