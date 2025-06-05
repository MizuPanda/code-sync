class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;

        if (nums.length > 0) {
            k++;
        }

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                    nums[k] = nums[i]; 
                    k++;
            }
        }

        return k;
    }
}