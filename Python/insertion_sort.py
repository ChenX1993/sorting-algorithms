def insertion_sort(arr):
    for i in range(len(arr)):
        curt = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    insertion_sort(arr)
    print(arr)
