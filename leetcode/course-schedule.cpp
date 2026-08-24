class Solution {
    
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> pre(numCourses);

        for (const vector<int>& preq : prerequisites) {
            pre.at(preq.at(0)).emplace_back(preq.at(1));
        }

        unordered_set<int> taken;

        for (int course = 0; course < numCourses; ++course) {
            if (!dfs(pre, taken, course)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(vector<vector<int>>& pre, unordered_set<int>& taken, const int course) {
        if (pre.at(course).empty()) {
            return true;
        }
    
        if (taken.contains(course)) {
            return false;
        }

        taken.insert(course);

        for (const int p : pre.at(course)) {
            if (!dfs(pre, taken, p)) {
                return false;
            }
        }

        pre.at(course) = {};

        return true;
    }
};