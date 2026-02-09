class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<string, int> letters;

        for (int i = 0; i < magazine.length(); ++i) {
            const string c = magazine.substr(i, 1);
            letters[c] += 1;
        }

        for (int i = 0; i < ransomNote.length(); ++i) {
            const string c = ransomNote.substr(i, 1);
            if (letters[c] < 1) {
                return false;
            } else {
                --letters[c];
            }
        }

        return true;
    }
};