def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            for j in range(i - gap, -1, -gap):
                if arr[j] > arr[j + gap]:
                    arr[j], arr[j + gap] = arr[j + gap], arr[j]
                else:
                    break
        gap = gap // 2


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    shell_sort(arr)
    print(arr)
