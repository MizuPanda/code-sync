class Solution {
public:
    int trap(vector<int>& height) {
        int water = 0;

        int leftBar = 0;
        int rightBar = height.size() - 1;

        int leftMax = height.at(leftBar);
        int rightMax = height.at(rightBar);

        while (leftBar < rightBar) {

            if (leftMax <= rightMax) {
                ++leftBar;

                if (height.at(leftBar) > leftMax) {
                    leftMax = height.at(leftBar);
                } else if (height.at(leftBar) < leftMax) {
                    water += leftMax - height.at(leftBar);
                }
            } else {
                --rightBar;

                if (height.at(rightBar) > rightMax) {
                    rightMax = height.at(rightBar);
                } else if (height.at(rightBar) < rightMax) {
                    water += rightMax - height.at(rightBar);
                }
            }
        }

        return water;
    }
};