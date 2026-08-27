class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        
        vector<int> curr = {0, 0, 0};

        for (const auto& triplet : triplets) {
            if (triplet.at(0) <= target.at(0) && triplet.at(1) <= target.at(1) && triplet.at(2) <= target.at(2)) {
                curr = {max(curr.at(0), triplet.at(0)), max(curr.at(1), triplet.at(1)), max(curr.at(2), triplet.at(2))};
            }
        }

        return curr == target;
    }
};