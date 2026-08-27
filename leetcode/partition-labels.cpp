class Solution {
public:
    vector<int> partitionLabels(string s) {
         
        vector<int> res;

        unordered_map<char, int> lastOcc;

        for (int i = 0; i < s.length(); ++i) lastOcc[s.at(i)] = i;

        int start = 0;
        int end = -1;

        for (int i = 0; i < s.length(); ++i) {
            
            end = max(end, lastOcc[s.at(i)]);

            if (i == end) {
                res.push_back(end - start + 1);
                start = end + 1;
            }
        }

        return res;
    }
};