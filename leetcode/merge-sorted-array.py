class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0) {
            return;
        } else if (m == 0) {
            for (int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }

            return;
        }

        int min = Math.min(nums1[0], nums2[0]);
        int max = Math.max(nums1[m - 1], nums2[n - 1]);

        int[] counters = new int[max - min + 1];

        for (int i = 0; i < m; i++) {
            counters[nums1[i] - min]++;
        }

        for (int numb : nums2) { // n time
            counters[numb - min]++;
        }

        int index = 0;

        for (int i = 0; i < counters.length; i++) { // m + n time
            for (int count = 0; count < counters[i]; count++) {
                nums1[index] = i + min;
                index++;
            }
        }
    }
}