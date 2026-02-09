class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<string, int> letterCount;

        for (int i = 0; i < s.length(); ++i) {
            const string ls = s.substr(i, 1);
            const string lt = t.substr(i, 1);

            ++letterCount[ls];
            --letterCount[lt];
        }

        for (auto count : letterCount) {
            if (count.second != 0)  {
                return false;
            }
        }

        return true;
    }
};