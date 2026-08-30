class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        

        auto isFeasible = [&time, &totalTrips](const long long minTime) -> bool {

            long long sumTrips = 0;

            for (int t : time) {

                sumTrips += minTime / t;

                if (sumTrips >= totalTrips) return true;
            }

            return false;
        };

        long long left = 1;
        long long right = 1e7 * totalTrips;
        long long ans = 1;

        while (left <= right) {

            long long mid = left + (right - left)/2;

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