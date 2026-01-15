class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> answer;

        stack<pair<int, int>> st;

        answer.emplace_back(0);
        st.push({temperatures.at(0), 0});

        for (int i = 1; i < temperatures.size(); ++i) {
        
            answer.emplace_back(0);

            while (!st.empty() && temperatures.at(i) > st.top().first) {
                answer.at(st.top().second) = (i - st.top().second);
                st.pop();
            }

            st.push({temperatures.at(i), i});
        }

        return answer;
    }
};