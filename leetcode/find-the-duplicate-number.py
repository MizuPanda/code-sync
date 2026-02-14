class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums.at(0);
        int fast = nums.at(0);

        while (true) {
            slow = nums.at(slow);
            fast = nums.at(nums.at(fast));

            if (slow == fast) {
                break;
            }
        }

        int slow2 = nums.at(0);

        while (slow != slow2) {
            slow = nums[slow];
            slow2 = nums[slow2];
        }

        return slow;
    }
};