def counting_sort(arr, exp):
    arr_len = len(arr)
    counts = [0 for _ in range(10)]
    outputs = ["" for _ in range(arr_len)]

    for num in arr:
        counts[(num // exp) % 10] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(arr_len - 1, -1, -1):
        num = arr[i]
        index = (num // exp) % 10
        outputs[counts[index] - 1] = num
        counts[index] -= 1

    for i in range(arr_len):
        arr[i] = outputs[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num > 0:
        counting_sort(arr, exp)
        exp *= 10
        max_num //= 10


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Array before sorting is: {arr}")
    radix_sort(arr)
    print(f"Array after sorting is: {arr}")
