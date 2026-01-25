class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());

        int start = 1;
        int end = piles.at(piles.size() - 1);
        
        while (end > start) {

            int k = start + (end - start)/2;

            int time = 0;

            for (int i = 0; i < piles.size(); ++i) {
                time += (piles.at(i) / k);
                if (piles.at(i) % k != 0) {
                    ++time;
                }

                if (time > h) {
                    start = k + 1;
                    break;
                }
            }

            if (time <= h) {
                end = k;
            }
        } 

        return start + (end - start)/2;
    }
};