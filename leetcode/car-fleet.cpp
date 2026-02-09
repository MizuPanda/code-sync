class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        stack<double> st;

        vector<pair<double, double>> cars;

        for (int i = 0; i < position.size(); ++i) {
            cars.push_back({position.at(i), speed.at(i)});
        }

        sort(cars.begin(), cars.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.first > b.first;
        });

        for (int i = 0; i < cars.size(); ++i) {
            const double time = (target - cars.at(i).first)/cars.at(i).second;

            if (st.empty() || st.top() < time) {
                st.push(time);
            }
        }

        return st.size();
    }
};