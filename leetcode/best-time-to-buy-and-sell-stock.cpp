class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf = 0;
        int sell = prices.at(0);
        int buy = prices.at(0);

        for (size_t i = 1; i < prices.size(); ++i) {
            const int stock = prices.at(i);

            if (stock < buy) {
                buy = stock;
                sell = stock;
            } else if (stock > sell) {
                sell = stock;

                const int profit = sell - buy;

                if (profit > maxProf) {
                    maxProf = profit;
                }
            }
        }

        return maxProf;
    }
};