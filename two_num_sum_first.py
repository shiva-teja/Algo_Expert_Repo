def two_num_sum(arr, total):
    for i in range(0, len(arr)-1):
        num1 = arr[i]
        for j in range(i+1, len(arr)):
            num2 = arr[j]
            if num1 + num2 == total:
                return[num1, num2]
    return []


array = [10, -4, 9, 23, 6]
target = 19
print(two_num_sum(array, target))

