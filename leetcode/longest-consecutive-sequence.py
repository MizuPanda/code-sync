class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set;
        int longest = 0;

        for (int num : nums) {
            num_set.insert(num);
        }

        for (auto it = num_set.begin(); it != num_set.end(); ++it) {
            const int num = *it;

            if (num_set.find(num - 1) == num_set.end()) {
                int length = 1;

                while (num_set.find(num + length) != num_set.end()) {
                    ++length;
                }

                longest = max(longest, length);
            } 
        }

        return longest;
    }
};