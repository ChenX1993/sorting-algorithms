"""
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects
having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object
in the output sequence.

Counting sort makes assumptions about the data, for example, it assumes that values are going to be in the range of
0 to 10 or 10 – 99 etc, Some other assumptions counting sort makes are input data will be all real numbers.

Like other algorithms this sorting algorithm is not a comparison-based algorithm, it hashes the value in a temporary
count array and uses them for sorting.

It uses a temporary array making it a non In Place algorithm.

Let us understand it with the help of an example.
"""
from typing import Union, List


def counting_sort(arr: Union[List[str], str]) -> list:
    arr_len = len(arr)
    outputs = ["" for _ in range(arr_len)]
    counts = [0 for _ in range(256)]

    for char in arr:
        counts[ord(char)] += 1

    for i in range(256):
        counts[i] += counts[i - 1]

    for i in range(arr_len):
        outputs[counts[ord(arr[i])] - 1] = arr[i]
        counts[ord(arr[i])] -= 1

    return outputs


if __name__ == "__main__":
    arr = "2345511"
    sorted_arr = counting_sort(arr)
    print(f"Array before sorting is: {arr}")
    print(f"Array after sorting is: {''.join(sorted_arr)}")
