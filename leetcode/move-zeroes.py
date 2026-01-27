class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int index = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums.at(i) != 0) {
                nums.at(index) = nums.at(i);
                ++index;
            }
        }

        for (int i = index; i < nums.size(); ++i) {
            nums.at(i) = 0;
        }
    }
};