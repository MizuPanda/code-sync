class Solution {
public:
    string longestPalindrome(string s) {
        string res;

        for (int i = 0; i < s.length(); ++i) {

            int left = i;
            int right = i;

            while (left >= 0 && right < s.length() && s.at(left) == s.at(right)) {
                --left;
                ++right;
            }

            if (right - left - 1 > res.length()) res = s.substr(left + 1, right - left - 1);

            left = i;
            right = i + 1;

            while (left >= 0 && right < s.length() && s.at(left) == s.at(right)) {
                --left;
                ++right;
            }

            if (right - left - 1 > res.length()) res = s.substr(left + 1, right - left - 1);

        }

        return res;
    }
};