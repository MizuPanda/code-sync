class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> newNums = {};
        const int s = nums.size();
        
        k = k % s;
        if (k == 0) {
            return ;
        }
        for (int i = 0; i < s; ++i) {
            if (i < k) {
                newNums.emplace_back(nums.at(s - k + i));
            } else {
                newNums.emplace_back(nums.at(i - k));
            }
        }

        nums = newNums;
    }
};