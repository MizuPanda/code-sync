class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());

        int start = 1;
        int end = piles.at(piles.size() - 1);
        
        while (end > start) {

            const int k = (start + end)/2;

            int time = 0;

            for (int i = piles.size() - 1; i >= 0; --i) {
                time += ceil((double) piles.at(i) / (double) k);

                if (time > h) {
                    start = k + 1;
                    break;
                }
            }

            if (time <= h) {
                end = k;
            }
        } 

        return (start + end)/2;
    }
};