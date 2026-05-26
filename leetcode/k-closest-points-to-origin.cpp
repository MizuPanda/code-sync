class Solution {
private:
    static double distance(const vector<int>& point) {
        return sqrt(pow(point.at(0), 2) + pow(point.at(1), 2));
    }

    struct PointCompare {
        bool operator()(const vector<int>& a, const vector<int>& b) {
            return distance(a) < distance(b);
        }
    };

public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, PointCompare> maxHeap;

        for (vector<int> point : points) {
            if (maxHeap.size() < k) {
                maxHeap.push(point);
            } else {
                const double dist = distance(point);
                const double topDist = distance(maxHeap.top());
                
                if (dist < topDist) {
                    maxHeap.pop();
                    maxHeap.push(point);
                }
            }
        }

        vector<vector<int>> res;

        while (!maxHeap.empty()) {
            res.push_back(maxHeap.top());
            maxHeap.pop();
        }

        return res;
    }
};