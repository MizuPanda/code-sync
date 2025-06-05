class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;
        int i = nums.size() - 2;
        
        if (nums.size() == 1) {
            return true;
        }

        while (i >= 0) {
            if (nums[i] >= goal - i) {
                goal = i;
            }

            --i;
        }

        return goal == i + 1;
    }
};