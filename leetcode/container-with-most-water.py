class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;

        int maxArea = min(height.at(start), height.at(end)) * (end - start);

        while (start < end) {
        
            if (height.at(start) <= height.at(end)) {
                ++start;
            } else {
                --end;
            }

            const int area = min(height.at(start), height.at(end)) * (end - start);

            if (area > maxArea) {
                maxArea = area;
            }
        }

        return maxArea;
    }
};