bool moreFrequent(const pair<int, int>& a, const pair<int,int>& b) {
        return a.second < b.second;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> mostFrequent;
        unordered_map<int, int> count;

        for (int num : nums) {
            ++count[num];
        }

        vector<pair<int, int>> countHeap;

        for (auto& c : count) {
            countHeap.push_back(c);

            push_heap(countHeap.begin(), countHeap.end(), moreFrequent);
        }

        while (mostFrequent.size() < k) {
            pop_heap(countHeap.begin(), countHeap.end(), moreFrequent);

            mostFrequent.emplace_back(countHeap.back().first);

            countHeap.pop_back();
        }

        return mostFrequent;
    }
};