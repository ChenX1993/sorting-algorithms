

def bucekt_sort(arr):
    num_max = max(arr)
    num_min = min(arr)
    bucket_size = (num_max - num_min) // len(arr) + 1
    bucekt_num = (num_max - num_min) // bucket_size + 1

    buckets = []
    for _ in range(bucekt_num):
        buckets.append([])

    for num in arr:
        bucket_index = (num - num_min) // bucket_size
        buckets[bucket_index].append(num)

    for bucket in buckets:
        bucket.sort()

    count = 0
    for bucket in buckets:
        for num in bucket:
            arr[count] = num
            count += 1


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 10, 2]
    bucekt_sort(arr)
    print(arr)
