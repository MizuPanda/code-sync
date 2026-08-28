class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int diff = 0;
        int res = 0;

        unordered_map<int, int> diffOcc;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums.at(i) == 1) ++diff;
            else --diff;

            if (diffOcc.find(diff) == diffOcc.end()) diffOcc[diff] = i;
            
            if (diff == 0) res = i + 1;
            else res = max(res, i - diffOcc[diff]);
        }

        return res;
    }
};