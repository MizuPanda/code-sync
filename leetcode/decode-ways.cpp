class Solution {
public:
    int numDecodings(string s) {

        int current = 1;
        int prev = 1;
        int pen = 1;

        for (int i = s.size() - 1; i >= 0; --i) {
            if (s.at(i) == '0') current = 0;

            if (i + 1 < s.size() && (s.at(i) == '1' || 
                                    (s.at(i) == '2' && s.at(i + 1) >= '0' && s.at(i + 1) <= '6'))) {
                current += pen;
            }

            pen = prev;
            prev = current;
        }

        return current;
    }
};