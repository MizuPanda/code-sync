class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        string s;

        backtrack(digits, res, s, 0);

        return res;   
    }

    void backtrack(const string& digits, vector<string>& res, string& s, int index) {
        if (index == digits.length()) {
            res.push_back(s);

            return ;
        }

        const int digit = stoi(digits.substr(index, 1));
        char start = 'a';
        char end;

        if (digit < 7) {
            start += (digit - 2)*3;
            end = start + 3;
        } else if (digit == 7) {
            start = 'p';
            end = start + 4;
        } else if (digit == 8) {
            start = 't';
            end = start + 3;
        } else {
            start = 'w';
            end = start + 4;
        }


        while (start < end) {
            s += start;
            backtrack(digits, res, s, index + 1);
            s = s.substr(0, s.length() - 1);

            ++start;
        }
    }
};