class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {

        int res = 0;

        for (int m = 0; m < grid.size(); ++m) {
            for (int n = 0; n < grid.at(0).size(); ++n) {

                if (grid.at(m).at(n) == '1') {
                    ++res;
                    searchIsland(grid, m, n);
                } 
            }
        }

        return res;
    }

    void searchIsland(vector<vector<char>>& grid, const int m, const int n) {
        if (m < 0 || m >= grid.size() || n < 0 || n >= grid.at(0).size() || grid.at(m).at(n) == '0') {
            return ;
        } 

        grid.at(m).at(n) = '0';

        // Left
        searchIsland(grid, m - 1, n);
        // Right
        searchIsland(grid, m + 1, n);
        // Bottom
        searchIsland(grid, m, n + 1);
        // Top
        searchIsland(grid, m, n - 1);
    }
};