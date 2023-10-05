#first_nmbr>other nmbrs then count
#i++ 
def count_inversions(arr):
    n = len(arr)
    count = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
                
    return count
arr=list(map(int,input().split(",")))
print(count_inversions(arr))