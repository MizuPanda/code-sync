class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res(nums.size(), -1);

        stack<int> next;

        for (int i = nums.size() * 2 - 1; i >= 0; --i) {

            const int index = i % nums.size();

            while (!next.empty() && nums.at(index) >= next.top()) next.pop();

            if (!next.empty()) res.at(index) = next.top();

            next.push(nums.at(index));
        }

        return res;
    }
};