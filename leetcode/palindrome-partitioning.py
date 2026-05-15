class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> part;

        backtrack(s, res, part, 0);

        return res;
    }

    bool isPalindrome(const string& s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.at(left) != s.at(right)) {
                return false;
            }
            ++left;
            --right;
        }

        return true;
    }

    void backtrack(const string& s, vector<vector<string>>& res, vector<string>& part, int index) {
        if (index == s.length()) {
            res.push_back(part);

            return;
        }

        string curr;

        for (int i = index; i < s.length(); ++i) {
            curr += s.at(i);
            
            if (isPalindrome(curr)) {
                part.push_back(curr);

                backtrack(s, res, part, i + 1);

                part.pop_back();
            }
        }
    }
};