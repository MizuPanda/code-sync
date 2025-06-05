class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<string, string> mapping;
        unordered_map<string, string> mapping2;
        
        for (int i = 0; i < s.length(); ++i) {
            const string s1 = s.substr(i, 1);
            const string t1 = t.substr(i, 1);

            if (mapping.find(s1) == mapping.end()) {
                mapping[s1] = t1;
            } 
            if (mapping2.find(t1) == mapping2.end()) {
                mapping2[t1] = s1;
            }
            
            if (mapping[s1] != t1 || mapping2[t1] != s1) {
                return false;
            }
        }

        return true;
    }
};