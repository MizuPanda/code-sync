class Solution {
private:
    int distance(const vector<int>& p1, const vector<int>& p2) const {
        return abs(p1.at(0) - p2.at(0)) + abs(p1.at(1) - p2.at(1));
    }

public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        
        int minCost = 0;

        unordered_set<int> visited;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        unordered_map<int, int> cache;
        pq.emplace(0, 0);

        while (!pq.empty()) {
            pair<int, int> edge = pq.top();
            pq.pop();

            int cost = edge.first;
            int u = edge.second;

            if (visited.contains(u)) continue;

            visited.insert(u);
            minCost += cost;

            for (int v = 0; v < points.size(); ++v) {
                if (!visited.contains(v)) {
                    int dist = distance(points.at(u), points.at(v));

                    if (cache.find(v) == cache.end() || dist < cache[v]) {
                        cache[v] = dist;
                        pq.emplace(dist, v);
                    }  
                }
            }
        }
        
        return minCost;
    }
};