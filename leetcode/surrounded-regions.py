class Solution {
public:
    void solve(vector<vector<char>>& board) {

        for (int m = 0; m < board.size(); ++m) {
            dfs(board, m, 0);
            dfs(board, m, board.at(0).size() - 1);
        }

        for (int n = 0; n < board.at(0).size(); ++n) {
            dfs(board, 0, n);
            dfs(board, board.size() - 1, n);
        }

        for (int m = 0; m < board.size(); ++m) {
            for (int n = 0; n < board.at(0).size(); ++n) {
                if (board.at(m).at(n) == 'O') {
                    board.at(m).at(n) = 'X';
                } else if (board.at(m).at(n) == 'B') {
                    board.at(m).at(n) = 'O';
                }
            }
        }
    }

    void dfs(vector<vector<char>>& board, const int m, const int n) {

        if (board.at(m).at(n) != 'O') return ;
    
        board.at(m).at(n) = 'B';

        if (m > 0) dfs(board, m - 1, n);
        if (m < board.size() - 1) dfs(board, m + 1, n);
        if (n > 0) dfs(board, m, n - 1);
        if (n < board.at(0).size() - 1) dfs(board, m, n + 1);
        
    }
};