package Java;

import java.util.Arrays;

class CountingSort {
    public void sort(char[] arr) {
        int[] counts = new int[256];
        char[] outputs = new char[arr.length];

        for (char c : arr) {
            counts[c]++;
        }

        for (int i = 1; i < 256; i++) {
            counts[i] += counts[i - 1];
        }

        for (int i = 0; i < arr.length; i++) {
            outputs[--counts[arr[i]]] = arr[i];
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i] = outputs[i];
        }
    }

    public static void main(String args[]) {
        CountingSort cs = new CountingSort();
        char[] arr = { 'b', 'b', 'c', 'a', 'c', 'e' };
        cs.sort(arr);

        System.out.println("Array after sort is: " + Arrays.toString(arr));
    }
}
