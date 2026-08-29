class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> res;
        stack<int> dec;

        unordered_map<int, int> idxMap;

        for (int i = nums2.size() - 1; i >= 0; --i) {

            while (!dec.empty() && nums2.at(i) >= dec.top()) dec.pop();

            if (!dec.empty()) idxMap[nums2.at(i)] = dec.top();

            dec.push(nums2.at(i));
        }

        for (int num : nums1) {
            if (idxMap.find(num) != idxMap.end()) res.push_back(idxMap[num]);
            else res.push_back(-1);
        }

        return res;
    }
};