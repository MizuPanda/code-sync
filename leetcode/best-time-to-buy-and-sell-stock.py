class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyPrice = prices.at(0);
        int maxProfit = 0;

        for (int i = 1; i < prices.size(); ++i) {
            if (buyPrice > prices.at(i)) {
                buyPrice = prices.at(i);
            }

            maxProfit = max(maxProfit, prices.at(i) - buyPrice);
        }

        return maxProfit;
    }
};