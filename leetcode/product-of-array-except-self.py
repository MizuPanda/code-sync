class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       
        vector<int> prefix_product;
        vector<int> reverse_product;

        int productP = 1;
        int productR = 1;

        for (int i = 0; i < nums.size(); ++i) {
            productP *= nums.at(i);
            productR *= nums.at(nums.size() - 1 - i);

            prefix_product.emplace_back(productP);
            reverse_product.emplace_back(productR);
        } 

        vector<int> answer;

        for (int i = 0; i < nums.size(); ++i) {
            int num = 1;

            if (i != 0) {
                num *= prefix_product.at(i - 1);
            }
            if (i != nums.size() - 1) {
                num *= reverse_product.at(nums.size() - 2 - i);
            }

            answer.emplace_back(num);
        }

        return answer;
    }
};