class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> comb;

        sort(candidates.begin(), candidates.end());

        backtrack(candidates, target, res, comb, 0);

        return res;
    }

    void backtrack(const vector<int>& candidates, int target, vector<vector<int>>& res, vector<int>& comb, int index) {
        if (target < 0) {
            return ;
        } else if (target == 0) {
            res.push_back(comb);
            return ;
        }

        for (int i = index; i < candidates.size(); ++i) {
            if (i > index && candidates.at(i) == candidates.at(i - 1)) {
                continue;
            }

            if (candidates.at(i) > target) {
                break;
            }
            comb.emplace_back(candidates.at(i));
            backtrack(candidates, target - candidates.at(i), res, comb, i + 1);
            comb.pop_back();
        }
    }
};