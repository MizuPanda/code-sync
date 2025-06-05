class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;

        int last = 0;
        int previous = last;

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                last = nums[i];
                k++;
            } else {
                if (i == 1 || last != nums[i] || previous != last) {
                    nums[k] = nums[i];
                    k++;
                }

                previous = last;
                last = nums[i];
            } 
        } 

        return k;
    }
}