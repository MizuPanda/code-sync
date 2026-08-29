class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int> maxHeap;

        for (int i = 0; i < heights.size() - 1; ++i) {
            const int jump = heights.at(i + 1) - heights.at(i);

            if (jump <= 0) continue;
            
            bricks -= jump;
            maxHeap.push(jump);

            if (bricks < 0) {
                if (ladders == 0) return i;

                --ladders;
                bricks += maxHeap.top();
                maxHeap.pop();
            }
        }

        return heights.size() - 1;
    }
};