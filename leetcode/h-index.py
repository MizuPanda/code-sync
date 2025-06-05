class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(), comp);

        int nonZero = 0;

        for (int i = 0; i < citations.size() && citations[i] != 0; ++i) {
            ++nonZero;
            if (i + 1 == citations[i]) {
                return citations[i];
            } else if (i + 1 > citations[i]) {
                return i;
            }
        }

        
        return citations.front() == 0? 0 : nonZero;
    }

    static bool comp(int a, int b) {
        return a > b;
    }
};