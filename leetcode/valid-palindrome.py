class Solution {
public:

    bool isPalindrome(string s) {
        int start = 0;
        int end = s.length() - 1;

        while (end > start) {
            const char startChar = s.at(start);
            const char endChar = s.at(end);

            if (!isAlphanumeric(startChar)) {
                ++start;
            } else if (!isAlphanumeric(endChar)) {
                --end;
            } else if (isSameChars(startChar, endChar)) {
                ++start;
                --end;
            } else {
                return false;
            }
        }

        return true;
    }

    bool isAlphanumeric(char x) {
        return (x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z') || (x >= '0' && x <= '9');
    }

    bool isSameChars(char x, char y) {

        const char diff = 'a' - 'A';

        if (x >= 'A' && x <= 'Z') {
            x += diff;
        }
        if (y >= 'A' && y <= 'Z') {
            y += diff;
        }
        
        return x == y;
    }
};