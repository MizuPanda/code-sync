class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if ((long long) m * k > bloomDay.size()) return -1;

        int left = 1;
        int right = 1e9;

        auto canMakeBouquet = [&bloomDay, &k, &m](const int day) -> bool {
            int total = 0;

            for (int i = 0; i < bloomDay.size(); ++i) {
                int count = 0;

                while (i < bloomDay.size() && count < k && bloomDay.at(i) <= day) {
                    ++count;
                    ++i;
                }

                if (count == k) {
                    ++total;
                    --i;
                }

                if (total >= m) return true;
            }

            return false;
        };

        while (left < right) {
            const int mid = left + (right - left)/2;

            if (canMakeBouquet(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;

    }
};