class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        
        auto isFeasible = [&nums, &maxOperations](const double pen) -> bool {

            int sumOps = 0;

            for (int num : nums) {

                if (num > pen) {
                    sumOps += ceil(num/pen) - 1;
                    
                    if (sumOps > maxOperations) return false;
                }

            }

            return true;
        };

        int left = 1;
        int right = 1e9;

        int ans = 1;

        while (left <= right) {

            int mid = left + (right - left)/2;

            if (isFeasible(mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }

        }

        return ans;
    }
};