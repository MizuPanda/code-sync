class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<string, int> letters;
        unordered_map<string, int> words;

        string word = "";
        int index = 0;

        for (int i = 0; i < s.length(); ++i) {
            const string sub = s.substr(i, 1);

            if (sub != " " && i != s.length() - 1) {
                word += sub;
            } else {
                if (i == s.length() - 1) {
                    word += sub;
                }

                const string c = pattern.substr(index, 1);

                if (letters.find(c) == letters.end()) {
                    letters[c] = index;
                }
                if (words.find(word) == words.end()) {
                    words[word] = index;
                }

                if (words[word] != letters[c]) {
                    return false;
                }

                word = "";
                ++index;
            }
        }

        return index == pattern.length();
    }
    
};