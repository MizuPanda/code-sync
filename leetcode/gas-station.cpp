class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        int diff = 0;

        for (int i = 0; i < gas.size(); ++i) diff += gas.at(i) - cost.at(i);
        
        if (diff < 0) return -1;

        int currentGas = 0;
        int start = 0;

        for (int i = 0; i < gas.size(); ++i) {
            currentGas += gas.at(i) - cost.at(i);

            if (currentGas < 0) {
                currentGas = 0;
                start = i + 1;
            }
        }

        return start;
    }
};