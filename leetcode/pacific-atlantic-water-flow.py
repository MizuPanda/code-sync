class Solution {
private:
    class PairMap {
    private:
        unordered_map<int, unordered_set<int>> v;
        int c = 0;

    public:
        unordered_map<int, unordered_set<int>> get() const {
            return v;
        }

        int count() const {
            return c;
        }

        bool find(const int m, const int n) const {
            return v.find(m) != v.end() && v.find(m)->second.contains(n);
        }

        void add(const int m, const int n) {
            if (v.find(m) == v.end()) {
                v[m] = {};
            }
            if (!v[m].contains(n)) {
                v[m].insert(n);
            }
            ++c;
        }
        
    };

    void dfs(const vector<vector<int>>& heights, const int m, const int n, PairMap& visit, const int prevHeight) {
        if (heights.at(m).at(n) < prevHeight || visit.find(m, n)) return ;

        visit.add(m, n);

        if (m > 0) dfs(heights, m - 1, n, visit, heights.at(m).at(n));
        if (m < heights.size() - 1) dfs(heights, m + 1, n, visit, heights.at(m).at(n));
        if (n > 0) dfs(heights, m, n - 1, visit, heights.at(m).at(n));
        if (n < heights.at(0).size() - 1) dfs(heights, m, n + 1, visit, heights.at(m).at(n));
    }

    vector<vector<int>> getResult(const PairMap& a, const PairMap& b) {
        vector<vector<int>> res;

        for (const auto& px : a.get()) {
            for (const int& py : px.second) {
                if (b.find(px.first, py)) {
                    res.push_back({px.first, py});
                }
            }
        }

        return res;
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        PairMap pac;
        PairMap atl;

        for (int m = 0; m < heights.size(); ++m) {
            dfs(heights, m, 0, pac, 0);
            dfs(heights, m, heights.at(0).size() - 1, atl, 0);
        }

        for (int n = 0; n < heights.at(0).size(); ++n) {
            dfs(heights, 0, n, pac, 0);
            dfs(heights, heights.size() - 1, n, atl, 0);
        }

        return pac.count() < atl.count() ? getResult(pac, atl) : getResult(atl, pac);
    }

};