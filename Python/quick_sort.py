def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, start, end):
    if start >= end:
        return
    pivot = start
    pos = start
    for i in range(start + 1, end + 1):
        if arr[i] <= arr[pivot]:
            pos += 1
            arr[i], arr[pos] = arr[pos], arr[i]
    arr[pivot], arr[pos] = arr[pos], arr[pivot]

    quick_sort_helper(arr, start, pos - 1)
    quick_sort_helper(arr, pos + 1, end)


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    quick_sort(arr)
    print(arr)
