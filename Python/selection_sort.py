def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swamp
        tmp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = tmp


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    selection_sort(arr)
    print(arr)
