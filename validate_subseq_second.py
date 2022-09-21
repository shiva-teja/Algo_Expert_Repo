def validate_sub_seq(array, seq_arr):
    seq_idx = 0
    for value in array:
        if seq_idx == len(seq_arr):
            break
        if value == seq_arr[seq_idx]:
            seq_idx += 1
    return seq_idx == len(seq_arr)


arr1 = [10, 8, -1, 4, 9, 11]
seq_arr1 = [8, 4, 11]
print(validate_sub_seq(arr1, seq_arr1))
