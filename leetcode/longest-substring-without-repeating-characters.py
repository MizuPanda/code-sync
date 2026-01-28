class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<string, int> dupMap;
       
        int leftIndex = 0;
        int rightIndex = 0;

        int longest = 0;

        while (rightIndex < s.length()) {
            const string c = s.substr(rightIndex, 1);

            if (dupMap.find(c) != dupMap.end() && dupMap[c] >= leftIndex) {
                longest = max(longest, rightIndex - leftIndex);
                leftIndex = dupMap[c] + 1;
            } 

            dupMap[c] = rightIndex;
            ++rightIndex;
        }

        return max(longest, rightIndex - leftIndex);
    }
};