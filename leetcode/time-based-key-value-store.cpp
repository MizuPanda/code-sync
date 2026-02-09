class TimeMap {
private:
    unordered_map<string, vector<pair<string, int>>> timeMap;

public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        if (timeMap.find(key) == timeMap.end()) {
            timeMap[key] = {};
        }
        
        timeMap[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {        
        if (timeMap.find(key) == timeMap.end()) {
            return "";
        } 

        int start = 0;
        int end = timeMap[key].size() - 1;

        while (end >= start) {
            const int index = (start + end)/2;
            const auto p = timeMap[key].at(index);

            if (p.second == timestamp) {
                return p.first;
            } else if (p.second > timestamp) {
                end = index - 1;
            } else if (index == end || timeMap[key].at(index + 1).second > timestamp) {
                return p.first;
            } else {
                start = index + 1;
            }
        }

        return "";
    }
};