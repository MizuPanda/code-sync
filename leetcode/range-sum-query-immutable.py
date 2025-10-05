class NumArray {
private:
    vector<int> sums;
public:
    NumArray(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            sums.emplace_back(nums.at(i));
            if (i != 0) {
                sums.at(i) += sums.at(i - 1);
            }
        }
    }
    
    int sumRange(int left, int right) {
        if (left == 0) {
            return sums.at(right);
        }

        return sums.at(right) - sums.at(left - 1);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */