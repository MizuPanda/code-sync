class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<int>> words;

        for (int i = 0; i < strs.size(); ++i) {
            string word = strs.at(i);

            sort(word.begin(), word.end());

            words[word].emplace_back(i);
        }

        vector<vector<string>> anagrams;

        for (auto wordMap : words) {
            const vector<int> indexes = wordMap.second;
            vector<string> group;

            for (int index : indexes) {
                group.emplace_back(strs.at(index));
            }

            anagrams.emplace_back(group);
        }

        return anagrams;
    }
};