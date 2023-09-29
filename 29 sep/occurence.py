def findSingle(arr,n):
    res=arr[0]
    for i in range(1,n):
        res=res^arr[i]
    return res
arr=[2,3,5,4,5,3,4,2,88,92]
n=len(arr)
print(findSingle(arr,n))