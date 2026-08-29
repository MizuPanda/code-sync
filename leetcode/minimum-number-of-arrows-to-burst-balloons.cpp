class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a.back() < b.back();
        });

        int index = 0;
        int count = 0;

        while (index < points.size()) {
            int x = points.at(index).back();

            while (index < points.size() && x >= points.at(index).front() && x <= points.at(index).back()) ++index;

            ++count;
        }

        return count;
    }
};