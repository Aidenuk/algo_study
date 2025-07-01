

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

arr = [5,7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]


def create2dArr(arr, n):
    newarr = [None] * n  
    index = 0
    
    for i in range(n):
        if index >= len(arr):
            break
        newarr[i] = arr[index:index + (i + 1)]
        print(f'res:{arr[index:index + (i + 1)]}')
        index += (i + 1)

    return newarr

print(create2dArr(arr, 5))
