class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;

        backtrack(res, nums, path);

        return res;
    }

    void backtrack(vector<vector<int>>& res, const vector<int>& nums, vector<int>& path) {
        if (path.size() == nums.size()) {
            res.push_back(path);

            return ;
        }

        for (int num : nums) {
            auto it = find(path.begin(), path.end(), num);

            if (it != path.end()) {
                continue;
            }

            path.emplace_back(num);
            backtrack(res, nums, path);
            path.pop_back();
        }
       
    }
};