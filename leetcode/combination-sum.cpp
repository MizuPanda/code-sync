class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> subset;

        backtrack(candidates, res, subset, 0, 0, target);

        return res;
    }

    void backtrack(const vector<int>& candidates, vector<vector<int>>& res, vector<int>& subset, int sum, int index, const int target) {
        if (index == candidates.size() || sum > target) {
            return ;
        } else if (sum == target) {
            res.push_back(subset);
            return ;
        }

        // Include again
        subset.emplace_back(candidates.at(index));
        sum += candidates.at(index);

        backtrack(candidates, res, subset, sum, index, target);

        // Exclude go next
        subset.pop_back();
        sum -= candidates.at(index);

        backtrack(candidates, res, subset, sum, index + 1, target);
    }
};