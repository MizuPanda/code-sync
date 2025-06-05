class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int sell;
        int profit = 0;
        int maxProfit = 0;

        for (int i = 1; i < prices.size(); ++i) {
            sell = prices[i];

            // Worth to sell
            if (sell - buy > profit) {
                profit = sell - buy;
            } else {
                maxProfit += profit;
                profit = 0;
                buy = sell;
            }
       } 
       maxProfit += profit;

       return maxProfit;
    }
};