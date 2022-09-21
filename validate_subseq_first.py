def validate_sub_seq(array, seq_arr):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(seq_arr):
        if array[arr_idx] == seq_arr[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(seq_arr)


arr1 = [10, 8, -1, 4, 9, 11]
seq_arr1 = [8, 4, 11]
print(validate_sub_seq(arr1, seq_arr1))
