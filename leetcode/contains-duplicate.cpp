class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> count;

        for (int num : nums) {
            if (count.find(num) == count.end()) {
                count[num] = true;
            } else {
                return true;
            }
        }

        return false;
    }
};