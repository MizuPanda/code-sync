class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int time = 0;
        int freshOranges = 0;
        queue<pair<int, int>> q;
        
        for (int m = 0; m < grid.size(); ++m) {
            for (int n = 0; n < grid.at(0).size(); ++n) {
                if (grid.at(m).at(n) == 1) {
                    ++freshOranges;
                } else if (grid.at(m).at(n) == 2) {
                    q.push({m, n});
                }
            }
        }

        while (!q.empty() && freshOranges > 0) {

            const int len = q.size();

            for (int i = 0; i < len; ++i) {
                contaminate(grid, q, freshOranges);
            }

            ++time;
        }

        return freshOranges > 0 ? -1 : time;
    }

    void contaminate(vector<vector<int>>& grid, queue<pair<int,int>>& q, int& fresh) {
        const pair<int, int> rotten = q.front();
        q.pop();

        // LEFT
        if (rotten.first > 0 && grid.at(rotten.first - 1).at(rotten.second) == 1) {
            grid.at(rotten.first - 1).at(rotten.second) = 2;
            q.push({rotten.first - 1, rotten.second});
            --fresh;
        }

        // RIGHT
        if (rotten.first < grid.size() - 1 && grid.at(rotten.first + 1).at(rotten.second) == 1) {
            grid.at(rotten.first + 1).at(rotten.second) = 2;
            q.push({rotten.first + 1, rotten.second});
            --fresh;
        }

        // BOTTOM
        if (rotten.second < grid.at(0).size() - 1 && grid.at(rotten.first).at(rotten.second + 1) == 1) {
            grid.at(rotten.first).at(rotten.second + 1) = 2;
            q.push({rotten.first, rotten.second + 1});
            --fresh;
        }

        // TOP
        if (rotten.second > 0 && grid.at(rotten.first).at(rotten.second - 1) == 1) {
            grid.at(rotten.first).at(rotten.second - 1) = 2;
            q.push({rotten.first, rotten.second - 1});
            --fresh;
        } 
    }
};