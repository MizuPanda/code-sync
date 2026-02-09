class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int currentPrice = prices.at(0);

        for (size_t i = 1; i < prices.size(); ++i) {
            int dayPrice = prices.at(i);

            if (dayPrice > currentPrice) {
                max += dayPrice - currentPrice;
            }

            currentPrice = dayPrice;
        }

        return max;
    }
};