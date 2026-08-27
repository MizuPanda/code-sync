class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums.front();
        if (nums.size() == 2) return max(nums.front(), nums.back());

        int maxStart2 = nums.front();
        int maxStart1 = max(maxStart2, nums.at(1));
        int currStart = max(maxStart1, maxStart2);

        int maxEnd2 = nums.at(1);
        int maxEnd1 = max(maxEnd2, nums.at(2));
        int currEnd = max(maxEnd1, maxEnd2);

        for (int i = 2; i < nums.size() - 1; ++i) {
            currStart = max(maxStart1, nums.at(i) + maxStart2);
            currEnd = max(maxEnd1, nums.at(i + 1) + maxEnd2);

            maxStart2 = maxStart1;
            maxStart1 = currStart;

            maxEnd2 = maxEnd1;
            maxEnd1 = currEnd;
        }

        return max(currStart, currEnd);
    }
};