class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {

        auto fitThreshold = [&nums, &threshold](const double div) -> bool {

            int sum = 0;

            for (int num : nums) sum += ceil(num/div);

            return sum <= threshold;

        };

        
        int left = 1;
        int right = 1e6;
        int ans = 1;

        while (left <= right) {

            int mid = left + (right - left)/2;

            if (fitThreshold(mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
};