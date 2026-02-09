class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        const int m = matrix.size();
        const int n = matrix.at(0).size();

        int start = 0;
        int end = m*n - 1;

        while (end >= start) {
            const int i = start + (end - start)/2;

            const int row = i / n;
            const int col = i % n;

            if (matrix.at(row).at(col) == target) {
                return true;
            } else if (matrix.at(row).at(col) < target) {
                start = i + 1;
            } else {
                end = i - 1;
            }
        }

        return false;
    }
};