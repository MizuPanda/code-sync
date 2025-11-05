class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, size_t> numbers;

        for (int i = 0; i < nums.size(); ++i) {
            const int num = nums.at(i);
            
            if (numbers.find(num) != numbers.end()) {
                vector<int> ans;

                ans.emplace_back(i);
                ans.emplace_back(numbers[num]);
                return ans;
            }

            numbers[target - num] = i;
        }

        return {};
    }
};