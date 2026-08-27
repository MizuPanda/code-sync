class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 1) return nums.at(0);
        else if (nums.size() == 2) return max(nums.at(0), nums.at(1));
        
        int curr = 0;
        int max2 = nums.at(0);
        int max1 = max(nums.at(1), max2);

        for (int i = 2; i < nums.size(); ++i) {
            curr = max(nums.at(i) + max2, max1);

            max2 = max1;
            max1 = curr; 
        }

        return curr;
    }
};