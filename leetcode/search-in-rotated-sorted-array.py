class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;

        while (end >= start) {
            const int index = (start + end)/2;

            if (nums.at(index) == target) {
                return index;
            } else if (target > nums.at(index)) {
                if (nums.at(index) > nums.at(end) || (nums.at(index) < nums.at(end) && nums.at(end) >= target)) {
                    start = index + 1;
                } else {
                    end = index - 1;
                }
            } else if (target < nums.at(index)) {
                if (nums.at(index) > nums.at(end) && target <= nums.at(end)) {
                    start = index + 1;
                } else {
                    end = index - 1;
                }
            } 
        }

        return -1;
    }
};