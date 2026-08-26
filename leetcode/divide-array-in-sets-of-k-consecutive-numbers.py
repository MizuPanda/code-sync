class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        map<int, int> c;

        for (int num : nums) ++c[num];

        for (const auto& [key, value] : c) {
            if (value > 0) {
                for (int i = k - 1; i >= 0; --i) {
                    if ((c[key + i] -= c[key]) < 0) return false;
                }
            }
        }

        return true;
    }
};