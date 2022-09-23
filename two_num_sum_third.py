def two_num_sum(arr, total):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        current_sum = arr[left] +arr[right]
        if current_sum == total:
            return [arr[left], arr[right]]
        elif current_sum < total:
            left += 1
        elif current_sum > total:
            right += 1

    return []


array = [10, -4, 9, 23, 6]
target = 19
print(two_num_sum(array, target))
