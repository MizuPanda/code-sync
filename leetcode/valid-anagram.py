class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<string, int> letterCount;

        for (int i = 0; i < s.length(); ++i) {
            const string letter = s.substr(i, 1);

            if (letterCount.find(letter) == letterCount.end()) {
                letterCount[letter] = 0;
            }

            ++letterCount[letter];
        }

        for (int i = 0; i < t.length(); ++i) {
            const string letter = t.substr(i, 1);

            if (letterCount.find(letter) == letterCount.end() || letterCount[letter] == 0) {
                return false;
            }

            --letterCount[letter];
        }

        return true;
    }
};