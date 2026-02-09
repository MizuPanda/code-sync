class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs.at(0);

        for (int i = 1; i < strs.size(); ++i) {
            const string str = strs.at(i);
            string newPrefix;

            for (int j = 0; j < str.length(); ++j) {
                const string ch = prefix.substr(j, 1);

                if (ch == str.substr(j, 1)) {
                    newPrefix += ch; 
                } else {
                    break;
                }
            }

            prefix = newPrefix;

            if (prefix.empty()) {
                break;
            }
        }

        return prefix;
    }
};