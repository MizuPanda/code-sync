class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> map = {};

        for (int i = 0; i < nums.size(); ++i) {
            if (map.find(nums.at(i)) == map.end()) {
                map[nums.at(i)] = 0;
            }

            ++map[nums.at(i)];
            if (map[nums.at(i)] > nums.size()/2) {
                return nums.at(i);
            }
        }

        return 0;
    }
};