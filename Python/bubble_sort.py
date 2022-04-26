def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    bubble_sort(arr)
    print(arr)
