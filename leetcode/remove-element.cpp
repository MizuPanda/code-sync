class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums.at(i) != val) {
                nums.at(k) = nums.at(i);
                ++k;
            }
        }

        return k;
    }
};