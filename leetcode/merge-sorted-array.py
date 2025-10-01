class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int right = m + n - 1;
        int index = n - 1;
        int left = m - 1;

        while (index >= 0) {
            if (left < 0 || nums2.at(index) >= nums1.at(left)) {
                nums1.at(right) = nums2.at(index);
                --index;
            } else {
                nums1.at(right) = nums1.at(left);
                --left;
            }
            --right;
        }
    }
};