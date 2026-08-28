class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        const int MAX = 2e9;

        vector<int> prices(n, MAX);
        prices.at(src) = 0;

        vector<int> tempPrices = prices;

        for (int i = 0; i < k + 1; ++i) {

            for (const vector<int>& flight : flights) {
                const int s = flight.at(0);
                const int d = flight.at(1);
                const int p = flight.at(2);
                
                if (prices.at(s) == MAX) continue;

                if (tempPrices.at(d) > prices.at(s) + p) {
                    tempPrices.at(d) = prices.at(s) + p;
                }
            }

            prices.swap(tempPrices);
        }

        return prices.at(dst) == MAX ? -1 : prices.at(dst);
    }
};