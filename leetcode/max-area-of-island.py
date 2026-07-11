class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;

        for (int m = 0; m < grid.size(); ++m) {
            for (int n = 0; n < grid.at(0).size(); ++n) {
                if (grid.at(m).at(n) == 1) {
                    maxArea = max(maxArea, findMaxArea(grid, m, n));
                }
            }
        }

        return maxArea;
    }

    int findMaxArea(vector<vector<int>>& grid, const int m, const int n) {
        
        if (m < 0 || m >= grid.size() || n < 0 || n >= grid.at(0).size() || grid.at(m).at(n) == 0) {
            return 0;
        }

        int area = 1;

        grid.at(m).at(n) = 0;

        // LEFT
        area += findMaxArea(grid, m - 1, n);
        // RIGHT
        area += findMaxArea(grid, m + 1, n);
        // TOP
        area += findMaxArea(grid, m, n - 1);
        // DOWN
        area += findMaxArea(grid, m, n + 1);

        return area;        
    }
};