class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        long long sum = 0;
        int left = 0;
        int maxFreq = 0;

        for (int right = 0; right < nums.size(); ++right) {
            sum += nums.at(right);

            while ((long long) nums.at(right) * (right - left + 1) - sum > k) {
                sum -= nums.at(left);
                ++left;
            }

            maxFreq = max(maxFreq, right - left + 1);
        }

        return maxFreq;
    }
};