class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(),greater<int>());

        int count = 0;

        for (size_t i = 0; i < citations.size(); ++i) {
            const int citation = citations.at(i);
            ++count;

            if (citation == 0) {
                --count;
                break;
            } else if (count > citation) {
                --count;
                return count;
            }
             else if (count == citation) {
                return count;
            }
        }

        return count;
    }
};