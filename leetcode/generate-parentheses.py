class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string s;

        backtrack(n, res, s, 0);

        return res;
    }

    void backtrack(const int n, vector<string>& res, string& s, const int numPar) {
        if (s.length() == n*2 || numPar > n || numPar < 0) {
            if (numPar == 0) {
                res.push_back(s);
            }

            return ;
        }

        s += "(";
        backtrack(n, res, s, numPar + 1);
        s.pop_back();

        s += ")";
        backtrack(n, res, s, numPar - 1);
        s.pop_back();
    }
};