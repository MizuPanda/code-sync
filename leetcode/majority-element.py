class Solution {
public:
    int majorityElement(vector<int>& nums) {
        const int majority = nums.size()/2;
        unordered_map<int, int> count;

        int maxCount = 0;
        int maxElement = 0;

        for (int num : nums) {
            if (count.find(num) == count.end()) {
                count[num] = 1;
            } else {
                ++count[num];
            }

            if (count[num] > maxCount) {
                maxCount = count[num];
                maxElement = num;

                if (maxCount > majority) {
                    break;
                }
            }
        }

        return maxElement;
    }
};