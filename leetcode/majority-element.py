class Solution {
public:
    int majorityElement(vector<int>& nums) {
        const int majority = nums.size()/2;
        unordered_map<int, int> count;

        for (int num : nums) {
            if (count.find(num) == count.end()) {
                count[num] = 0;
            }
            
            ++count[num];

            if (count[num] > majority) {
                return num;
            }
        }

        return 0;
    }
};