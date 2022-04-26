def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid_index = len(arr) // 2

    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    l_i, r_i, a_i = 0, 0, 0
    while l_i < len(left_arr) or r_i < len(right_arr):
        if l_i >= len(left_arr):
            arr[a_i] = right_arr[r_i]
            a_i += 1
            r_i += 1
            continue
        if r_i >= len(right_arr):
            arr[a_i] = left_arr[l_i]
            a_i += 1
            l_i += 1
            continue

        if right_arr[r_i] < left_arr[l_i]:
            arr[a_i] = right_arr[r_i]
            a_i += 1
            r_i += 1
        else:
            arr[a_i] = left_arr[l_i]
            a_i += 1
            l_i += 1


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    merge_sort(arr)
    print(arr)
