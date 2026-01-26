class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0;
        int end = nums.size() - 1;

        while (end > start) {
           const int index = (start + end)/2;

           if (nums.at(index) > nums.at(end)) {
                start = index + 1;
           } else {
                end = index;
           }
        }

        return nums.at(end);
    }
};