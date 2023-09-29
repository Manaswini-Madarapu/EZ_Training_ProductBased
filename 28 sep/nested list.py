def generate_list(n):
    tl=[]
    for num in range(n):
        row=[]
        for i in range(n):
            row.append(i)
        tl.append(row)
    return tl
print(generate_list())