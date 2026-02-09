class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        const int n = nums.size();
        int farthest = 0;
        int end = 0;

        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] + i > farthest) {
                farthest = nums[i] + i;
            }

            if (i == end) {
                ++jumps;
                end = farthest;

                if (end >= n - 1) {
                    break;
                }
            }
        }

        return jumps;
    }
};