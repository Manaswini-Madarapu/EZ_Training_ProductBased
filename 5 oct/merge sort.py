def merge_sort(arr):
    # Base case: If the input list has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
            print(result)
        else:
            result.append(right[right_index])
            right_index += 1
            print(result)
    result.extend(left[left_index:])
    
    result.extend(right[right_index:])
    return result

my_list = [14, 8, 2, 9, 69, 1]
sorted_list = merge_sort(my_list)
print(sorted_list)


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i += 1
                k += 1
            else:
                arr[k]=right[j]


























