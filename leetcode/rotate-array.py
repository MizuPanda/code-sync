class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        const vector<int> copy = nums;
        const int len = nums.size();

        for (size_t i = 0; i < len; ++i) {
            const int pos = (i + k) % len;

            nums.at(pos) = copy.at(i);
        }
    }
};