class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<string, int> s1Map;
        unordered_map<string, int> s2Map;

        for (int i = 0; i < s1.length(); ++i) {
            const string c = s1.substr(i, 1);

            if (s1Map.find(c) == s1Map.end()) {
                s1Map[c] = 0;
            } 

            ++s1Map[c];
        }

        int left = 0;

        for (int right = 0; right < s2.length(); ++right) {
            const string c = s2.substr(right, 1);

            if (s2Map.find(c) == s2Map.end()) {
                s2Map[c] = 0;
            }

            ++s2Map[c];

            if (s1Map.find(c) == s1Map.end()) {
                s1Map[c] = 0;
            }

            while (s2Map[c] > s1Map[c]) {
                --s2Map[s2.substr(left, 1)];
                ++left;
            }

            if (right - left + 1 == s1.length()) {
                return true;
            }
        }

        return false;
    }
};