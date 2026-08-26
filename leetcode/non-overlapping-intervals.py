class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            return a.at(1) < b.at(1);
        });

        int backEnd = intervals.at(0).at(1);
        int count = 0;

        for (int i = 1; i < intervals.size(); ++i) {
            if (backEnd > intervals.at(i).at(0)) {
                ++count;
            } else {
                backEnd = intervals.at(i).at(1);
            }
        }

        return count;
    }
};