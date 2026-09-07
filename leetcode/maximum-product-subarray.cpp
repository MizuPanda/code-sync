class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums.front();

        int currMax = 1;
        int currMin = 1;
        
        for (int num : nums) {
            int temp = currMax * num;

            currMax = max({temp, currMin * num, num});
            currMin = min({temp, currMin * num, num});

            res = max(res, currMax); 
        }

        return res;
    }
};