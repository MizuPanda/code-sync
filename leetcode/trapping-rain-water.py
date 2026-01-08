class Solution {
public:
    int trap(vector<int>& height) {
        int numRain = 0;

        for (int i = 0; i < height.size() - 1; ++i) {
            if (height.at(i) == 0 || height.at(i + 1) >= height.at(i)) continue;

            int bottom = height.at(i + 1);

            for (int j = i + 2; j < height.size(); ++j) {

                if (height.at(j) > bottom) {
                    numRain += (j - i - 1)*(min(height.at(i), height.at(j)) - bottom);
                    if (height.at(j) > height.at(i)) {
                        break;
                    } else {
                        bottom = height.at(j);
                    }
                }
            }

        }

        return numRain;
    }
};