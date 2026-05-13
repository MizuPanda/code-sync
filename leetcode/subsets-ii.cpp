class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> sub;

        sort(nums.begin(), nums.end());

        backtrack(nums, res, sub, 0);

        return res;
    }

    void backtrack(const vector<int>& nums, vector<vector<int>>& res, vector<int>& sub, int index) {
        if (index == nums.size()) {
            res.push_back(sub);

            return ;
        }

        sub.emplace_back(nums.at(index));
        backtrack(nums, res, sub, index + 1);
        sub.pop_back();
        while (index + 1 < nums.size() && nums.at(index) == nums.at(index + 1)) {
            ++index;
        }
        backtrack(nums, res, sub, index + 1);
    }
};