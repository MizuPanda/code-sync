class Solution {
public:
    bool canPartition(vector<int>& nums) {

        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (sum % 2 != 0) return false;

        sum /= 2;

        unordered_set<int> dp = {0};
        unordered_set<int> nextDP = {0};

        for (int i = nums.size() - 1; i >= 0; --i) {

            for (int t : dp) {
                if (t + nums.at(i) <= sum) nextDP.insert(t + nums.at(i));  
                nextDP.insert(t);
            } 

            dp.swap(nextDP);
        }

        return dp.contains(sum);
    }
};