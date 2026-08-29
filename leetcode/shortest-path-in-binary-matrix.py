class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {

        const int N = grid.size();

        queue<array<int, 3>> q;
        q.push({0, 0, 1});

        const vector<pair<int,int>> dir = {{-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}};

        while (!q.empty()) {
            auto [r, c, length] = q.front(); 
            q.pop();
            
            if (grid.at(r).at(c) == 1) continue;
            if (r == N - 1 && c == N - 1) return length;

            grid.at(r).at(c) = 1;

            for (const auto& [dr, dc] : dir) {

                int nr = r + dr;
                int nc = c + dc;

                if (min(nr, nc) < 0 || max(nr, nc) >= N || grid.at(nr).at(nc) == 1) continue;

                if (grid.at(nr).at(nc) == 0) {
                    q.push({nr, nc, length + 1});
                }
            }
        }

        return -1;
    }
};