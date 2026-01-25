class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;

        while (end >= start) {
            const int index = start + (end - start)/2;

            if (nums.at(index) == target) {
                return index;
            } else if (nums.at(index) < target) {
                start = index + 1;
            } else {
                end = index - 1;
            }
        }

        return -1;
    }
};