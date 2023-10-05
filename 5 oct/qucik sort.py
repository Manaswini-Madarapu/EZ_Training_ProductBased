def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    return left_sorted + middle + right_sorted

my_list = list(map(int,input().split(",")))
sorted_list = quick_sort(my_list)
print(sorted_list)





arr=list(map(int,input().split(",")))
if len(arr)<1:
    print(arr)
else:
    p=arr[0]
    left=[i for i in arr if i<p]
    right=[i for i in arr if i>p]
    x=(left+[p]+right)
print(x)
    