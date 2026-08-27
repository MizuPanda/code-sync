class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_map<string, bool> poss;

        auto isPossible = [&wordDict, &poss](this auto self, const string& str) -> bool {
            if (poss.find(str) != poss.end()) return poss[str];

            string curr = "";

            for (int i = 0; i < str.length(); ++i) {
                curr.push_back(str.at(i));

                for (const string& word : wordDict) {
                    if (curr == word && (curr.size() == str.size() || self(str.substr(i + 1)))) {
                        poss[curr] = true;
                        return true;
                    }
                }
            }

            poss[str] = false;

            return false;
        };

        return isPossible(s);
    }
};