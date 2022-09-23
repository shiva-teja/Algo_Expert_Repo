def sorted_squares(arr):
    sorted_arr = [0 for _ in arr]
    for i in range(len(arr)):
        value = arr[i]
        sorted_arr[i] = value * value
    sorted_arr.sort()
    return sorted_arr


array = [-1, 3, 9, 20]

print(sorted_squares(array))

