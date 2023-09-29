def sum_of_n_numbers(n):
    if n == 0:
        return 0  
    else:
        return n + sum_of_n_numbers(n - 1)
n = int(input())
result = sum_of_n_numbers(n)
print(result)
 # space complexity O(n)