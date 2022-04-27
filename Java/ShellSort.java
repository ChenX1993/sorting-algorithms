package Java;

import java.util.Arrays;

public class ShellSort {
    public void sort(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }

        int gap = arr.length / 2;
        while (gap > 0) {
            for (int i = gap; i < arr.length; i++) {
                for (int j = i - gap; j >= 0; j -= gap) {
                    if (arr[j] <= arr[j + gap]) {
                        break;
                    }
                    swap(arr, j, j + gap);
                }
            }
            gap = gap / 2;
        }
    }

    private void swap(int[] arr, int index1, int index2) {
        int tmp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = tmp;
    }

    public static void main(String args[]) {
        ShellSort ss = new ShellSort();
        int[] arr = { 5, 2, 8, 3, 6, 1 };
        ss.sort(arr);

        System.out.println("Array after sort is: " + Arrays.toString(arr));
    }

}
