class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int y = 0; y < board.size(); ++y) {
            for (int x = 0; x < board.at(0).size(); ++x) {
                if (backtrack(board, word, x, y, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    bool backtrack(vector<vector<char>>& board, const string& word, int x, int y, int index) {        
        bool isExist = false;

        if (board.at(y).at(x) == word.at(index)) {
            
            if (index + 1 == word.length()) {
                return true;
            }

            board.at(y).at(x) = '.';
                
            // Right
            ++x;
            if (x < board.at(0).size()) {
                isExist = backtrack(board, word, x, y, index + 1);
            }
            --x;

            // Left
            --x;
            if (!isExist && x >= 0) {
                isExist = backtrack(board, word, x, y, index + 1);
            }
            ++x;

            // Bottom
            ++y;
            if (!isExist && y < board.size()) {
                isExist = backtrack(board, word, x, y, index + 1);
            }
            --y;

            // Top
            --y;
            if (!isExist && y >= 0) {
                isExist = backtrack(board, word, x, y, index + 1);
            }
            ++y;

            board.at(y).at(x) = word.at(index);
        } 

        return isExist;
    }
};