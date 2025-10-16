class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 1;
        int index = 1;

        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums.at(i) == nums.at(i - 1)) {
                ++count;
            } else {
                count = 1;
            }

            if (count <= 2) {
                nums.at(index) = nums.at(i);
                ++index;
            }
        }

        return index;
    }
};