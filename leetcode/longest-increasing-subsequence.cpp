class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
    
        vector<int> dp;
        dp.emplace_back(1);
        int best = 1;

        for (int i = 1; i < nums.size(); ++i) {
            int longest = 1;

            for (int j = 0; j < i; ++j) {
                if (nums.at(j) < nums.at(i)) {
                    longest = max(longest, dp.at(j) + 1);
                }
            }

            best = max(best, longest);
            dp.emplace_back(longest);
        }

        return best;
    }
};