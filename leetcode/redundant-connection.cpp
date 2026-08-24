class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<vector<int>> graph(edges.size() + 1);

        auto isConnected = [&graph](int u, int v) {
            unordered_set<int> visited;
            stack<int> stack;

            stack.push(u);

            while (!stack.empty()) {
                const int node = stack.top();
                stack.pop();

                if (visited.contains(node)) continue;

                visited.insert(node);

                if (node == v) return true;

                for (int neighbor : graph.at(node)) stack.push(neighbor);
                
            }

            return false;
        };

        for (const vector<int>& edge : edges) {
            const int u = edge.at(0);
            const int v = edge.at(1);

            if (isConnected(u, v)) return edge;
            
            graph.at(u).push_back(v);
            graph.at(v).push_back(u);
        }

        return {};
    }
};