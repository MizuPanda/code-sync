class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        freq[0] = 1;

        int total = 0;
        int count = 0;

        for (int num : nums) {
            total += num;

            count += freq[total - k];

            ++freq[total];
        }

        return count;
    }
};