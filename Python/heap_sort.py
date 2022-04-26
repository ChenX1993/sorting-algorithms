def heap_sort(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def heapify(arr, len, root):
    if root >= len:
        return
    left = 2 * root + 1
    right = 2 * root + 2

    largest = root
    if left < len and arr[left] > arr[largest]:
        largest = left
    if right < len and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, len, largest)


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    heap_sort(arr)
    print(arr)
