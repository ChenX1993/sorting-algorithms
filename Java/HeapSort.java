package Java;

import java.util.Arrays;

class HeapSort {
    public void sort(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }

        for (int i = arr.length / 2; i >= 0; i--) {
            heapify(arr, arr.length - 1, i);
        }

        for (int i = arr.length - 1; i > 0; i--) {
            swap(arr, 0, i);
            heapify(arr, i - 1, 0);
        }
    }

    private void heapify(int[] arr, int end, int root) {
        if (root > end) {
            return;
        }
        int largest = root;
        int left = root * 2 + 1;
        int right = root * 2 + 2;
        if (left <= end && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right <= end && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != root) {
            swap(arr, largest, root);
            heapify(arr, end, largest);
        }
    }

    private void swap(int[] arr, int index1, int index2) {
        int tmp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = tmp;
    }

    public static void main(String args[]) {
        HeapSort hs = new HeapSort();
        int[] arr = { 5, 2, 8, 3, 6, 1 };
        hs.sort(arr);

        System.out.println("Array after sort is: " + Arrays.toString(arr));
    }
}
