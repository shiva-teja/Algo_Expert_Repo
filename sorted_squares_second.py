def sorted_squares(arr):
    sorted_arr = [0 for _ in arr]
    left = 0
    right = len(arr)-1
    for idx in reversed(range(len(arr))):
        if abs(arr[left]) > abs(arr[right]):
            sorted_arr[idx] = arr[left] * arr[left]
            left += 1
        else:
            sorted_arr[idx] = arr[right] * arr[right]
            right -= 1
    return sorted_arr


array = [-1, 3, 9, 20]

print(sorted_squares(array))
