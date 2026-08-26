class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> res;
        res.push_back(intervals.at(0));

        for (int i = 1; i < intervals.size(); ++i) {
            if (res.back().at(1) >= intervals.at(i).at(0)) {
                res.back().at(1) = max(res.back().at(1), intervals.at(i).at(1));
            } else {
                res.push_back(intervals.at(i));
            }
        }

        return res;
    }
};