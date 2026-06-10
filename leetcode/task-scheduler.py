class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int interval = 0;

        priority_queue<int> maxHeap;
        unordered_map<char, int> freq;
        queue<pair<int,int>> idle;

        for (int i = 0; i < tasks.size(); ++i) {
            const char c = tasks.at(i);

            if (freq.find(c) == freq.end()) {
                freq[c] = 0; 
            }

            ++freq[c];
        }

        for (const auto& it : freq) {
            maxHeap.push(it.second);
        }

        while (!maxHeap.empty() || !idle.empty()) {
            if (!idle.empty() && idle.front().second < interval) {
                maxHeap.push(idle.front().first);
                idle.pop();
            }
            
            if (maxHeap.size() > 0) {
                if (maxHeap.top() != 1) {
                    idle.push({maxHeap.top() - 1, interval + n});
                }
                maxHeap.pop();
            }
            ++interval;
        }

        return interval;
    }
};