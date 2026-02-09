class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int result = 0;
        int mostFreq = 0;
        unordered_map<string, int> freq;

        for (int right = 0; right < s.length(); ++right) {
            const string r = s.substr(right, 1);

            if (freq.find(r) == freq.end()) {
                freq[r] = 0;
            }

            ++freq[r];

            mostFreq = max(mostFreq, freq[r]);

            while (right - left + 1 - mostFreq > k) {
                --freq[s.substr(left, 1)];
                ++left;
            }

            result = max(result, right - left + 1);
        }

        return result;
    }
};