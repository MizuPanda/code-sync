class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
    
        unordered_map<string, bool> duplicateMap;

        vector<vector<int>> answer;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; ++i) {
            if (i > 0 && nums.at(i) == nums.at(i - 1)) continue;
            
            int start = i + 1;
            int end = nums.size() - 1;

            while (end > start) {
                const int sum = nums.at(i) + nums.at(start) + nums.at(end);

                if (sum > 0) {
                    --end;
                } else if (sum < 0) {
                    ++start;
                } else {
                    const string key = to_string(nums.at(i)) + to_string(nums.at(start)) + to_string(nums.at(end));
                    
                    if (duplicateMap.find(key) == duplicateMap.end()) {
                        duplicateMap[key] = true;
                        answer.push_back({nums.at(i), nums.at(start), nums.at(end)});
                    }

                    ++start;
                    --end;
                }
            }

        }

        return answer;
    }
};