class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        
        sort(position.begin(), position.end());

        auto isDistributable = [&position, &m](const int min) {

            int count = 1;
            int last = position.front();

            for (int i = 1; i < position.size(); ++i) {
                if (position.at(i) - last >= min) {
                    ++count;
                    last = position.at(i);
                }

                if (count >= m) return true;
            }

            return false;
        };

        int left = 0;
        int right = (position.back() - position.front())/(m - 1);

        int ans = 1;

        while (left <= right) {
            int mid = left + (right - left)/2;

            if (isDistributable(mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ans;

    }

};