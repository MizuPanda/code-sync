class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums.at(0);
        int bestSum = nums.at(0);

        for (int i = 1; i < nums.size(); ++i) {
            sum = max(sum + nums.at(i), nums.at(i));
            bestSum = max(bestSum, sum);
        }

        return bestSum;
    }
};