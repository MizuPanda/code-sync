class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n + 1, 2e9);
        vector<vector<pair<int, int>>> ajd(n + 1);

        for (const vector<int> time : times) ajd.at(time.at(0)).emplace_back(time.at(2), time.at(1));

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        dist.at(k) = 0;
        pq.emplace(0, k);

        while (!pq.empty()) {
            pair<int,int> top = pq.top();
            pq.pop();

            int u = top.second;
            int tu = top.first;

            if (tu > dist.at(u)) continue;

            for (pair<int, int>& pv : ajd.at(u)) {

                int v = pv.second;
                int tv = pv.first;

                if (dist.at(v) > dist.at(u) + tv) {
                    dist.at(v) = dist.at(u) + tv;
                    pq.emplace(dist.at(v), v);
                }

            }
        }

        int maxTime = dist.at(1);

        for (int i = 2; i < dist.size(); ++i) {
            maxTime = max(maxTime, dist.at(i));
        }

        return  maxTime == 2e9 ? -1 : maxTime;
        
    }
};