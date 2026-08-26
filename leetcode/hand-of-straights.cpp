class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        
        if (hand.size() % groupSize != 0) return false;

        auto findSuccessors = [&hand, &groupSize](int i) -> bool {
            int next = hand.at(i) + 1;
            hand.at(i) = -1;
            int count = 1;
            i += 1;

            while (i < hand.size() && count < groupSize) {
                if (hand.at(i) == next) {
                    next = hand.at(i) + 1;
                    hand.at(i) = -1;
                    ++count;
                }
                ++i;
            }

            return count == groupSize;
        };

        sort(hand.begin(), hand.end());

        for (int i = 0; i < hand.size(); ++i) {
            if (hand.at(i) >= 0 && !findSuccessors(i)) return false;
        }

        return true;
    }
};