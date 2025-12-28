class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        int end = numbers.size() - 1;

        while (end > start) {
            const int sum = numbers.at(start) + numbers.at(end);

            if (sum > target) {
                --end;
            } else if (sum < target) {
                ++start;
            } else {
                return {start + 1, end + 1};
            }
        }

        return {-1, -1};
    }
};