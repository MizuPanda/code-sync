class Solution {
public:
    int partitionString(string s) {
        int count = 0;
        unordered_set<char> seen;

        for (char c : s) {

            if (!seen.contains(c)) {
                seen.insert(c);
            } else {
                seen = {c};
                ++count;
            }
        }

        return count + 1;
    }
};