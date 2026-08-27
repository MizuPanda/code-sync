class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp.at(0) = 0;

        for (int a = 1; a < amount + 1; ++a) {
            for (int c : coins) {
                if (a - c >= 0) dp.at(a) = min(dp.at(a), 1 + dp.at(a - c));
            }
        }

        return dp.at(amount) == amount + 1 ? -1 : dp.at(amount);
    }
};