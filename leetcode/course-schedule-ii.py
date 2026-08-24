class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> pre(numCourses);
        vector<int> res;

        for (const vector<int>& prereq : prerequisites) {
            pre.at(prereq.at(0)).emplace_back(prereq.at(1));
        }

        unordered_set<int> taken;

        bool canFinish = true;

        for (int course = 0; course < numCourses && canFinish; ++course) {
            if (!dfs(pre, taken, course, res)) {
                canFinish = false;
            }
        }

        if (!canFinish) res = {};

        return res;
    }

    bool dfs(vector<vector<int>>& pre, unordered_set<int>& taken, const int course, vector<int>& res) {
        if (pre.at(course).empty()) {
            if (!taken.contains(course)) {
                res.emplace_back(course);
                taken.insert(course);
            }
            return true;
        }

        if (taken.contains(course)) {
            return false;
        }

        taken.insert(course);

        for (const int p : pre.at(course)) {
            if (!dfs(pre, taken, p, res)) {
                return false;
            }
        }

        pre.at(course) = {};
        res.emplace_back(course);

        return true;
    }
};