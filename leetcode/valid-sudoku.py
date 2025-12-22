class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        if (!isValidRows(board) || !isValidCols(board) || !isValidBoxes(board)) {
            return false;
        } 
        
        return true;
    }

    bool isValidRows(vector<vector<char>>& board) {
        
        for (int i = 0; i < 9; ++i) {
            unordered_map<char, bool> digits;

            vector<char> row = board.at(i);

            for (int j = 0; j < 9; ++j) {
                const char c = row.at(j);

                if (c >= '1' && c <= '9') {
                    if (digits.find(c) != digits.end() && digits[c]) {
                        return false;
                    } 

                    digits[c] = true;
                }
            }

            
        }

        return true;
    }

    bool isValidCols(vector<vector<char>>& board) {

        for (int col = 0; col < 9; ++col) {
            unordered_map<char, bool> digits;

            for (int row = 0; row < 9; ++row) {
                const char c = board.at(row).at(col);

                if (c >= '1' && c <= '9') {
                    if (digits.find(c) != digits.end() && digits[c]) {
                        return false;
                    } 

                    digits[c] = true;
                }
            }
        }

        return true;
    }

    bool isValidBoxes(vector<vector<char>>& board) {

        for (int box = 0; box < 9; ++box) {
            unordered_map<char, bool> digits;

            for (int cell = 0; cell < 9; ++cell) {
                
                const int row = cell/3 + 3*(box/3);
                const int col = (cell % 3) + 3*(box % 3);
                
                const char c = board.at(row).at(col);

                if (c >= '1' && c <= '9') {
                    if (digits.find(c) != digits.end() && digits[c]) {
                        return false;
                    } 

                    digits[c] = true;
                }
            }
        }

        return true;
    }

    
};