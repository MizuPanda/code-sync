class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        cost.emplace_back(0);

        for (int i = cost.size() - 4; i >= 0; --i) {
            cost.at(i) += min(cost.at(i + 1), cost.at(i + 2));
        }

        return min(cost.at(0), cost.at(1));
    }
};