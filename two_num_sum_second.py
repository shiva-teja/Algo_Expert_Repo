def two_num_sum(arr, total):
    nums = { }
    for num in array:
        if total-num in nums:
            return [total-num, num]
        else:
            nums[num] = True
    return[]


array = [10, -4, 9, 23, 6]
target = 19
print(two_num_sum(array, target))
