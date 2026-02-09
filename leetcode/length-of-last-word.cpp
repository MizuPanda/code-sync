class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream sock {s};

        string last;

        for (string str; sock >> str;) {
            last = str;
        }

        return last.length();
    }
};