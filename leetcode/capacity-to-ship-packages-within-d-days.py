class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        
        int left = 0;
        int right = 0;

        vector<int> prefix;

        for (int weight : weights) {
            left = max(weight, left);
            right += weight;

            prefix.push_back(right);
        }

        int ans;

        auto canDeliver = [&prefix, &days](const int capacity, const int n) -> bool {

            int currentCapacity = capacity;
            for (int day = 0; day < days; ++day) {
                const int index = upper_bound(prefix.begin(), prefix.end(), currentCapacity) - prefix.begin() - 1;

                if (index == n - 1) return true;
                
                currentCapacity = prefix.at(index) + capacity;
            }

            return false;
        };

        while (left <= right) {

            const int mid = left + (right - left)/2;

            if (canDeliver(mid, weights.size())) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
};