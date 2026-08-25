class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        sort(tiles.begin(), tiles.end());
        const int n = tiles.size();

        vector<int> prefix;
        vector<int> et;

        prefix.emplace_back(0);

        for (int i = 0; i < n; ++i) {
            prefix.emplace_back(prefix.at(i) + (tiles.at(i).at(1) - tiles.at(i).at(0) + 1));
            et.emplace_back(tiles.at(i).at(1));
        }

        int ans = 0;

        for (int i = 0; i < n; ++i) {
            int start = tiles.at(i).at(0);
            int end = start + carpetLen - 1;

            int index = upper_bound(et.begin(), et.begin() + n, end) - et.begin();

            int tsum = prefix.at(index) - prefix.at(i);

            if (index < n && end >= tiles.at(index).at(0)) tsum += end - tiles.at(index).at(0) + 1;

            ans = max(ans, tsum);
        }

        return ans;
    }
};