class Solution {
public:
    int strStr(string haystack, string needle) {
        for (int i = 0; (needle.length() + i) <= haystack.length(); ++i) {
            if (haystack.at(i) == needle.at(0)) {
                bool isNeedle = true;
                for (int j = 1; j < needle.length(); ++j) {
                    if (haystack.at(i + j) != needle.at(j)) {
                        isNeedle = false;
                        break;
                    }
                }

                if (isNeedle) {
                    return i;
                }
            }
        }

        return -1;
    }
};