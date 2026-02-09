class Solution {
public:
    int romanToInt(string s) {
        if (s.length() == 1) {
            if (s == "I") {
                return 1;
            } else if (s == "V") {
                return 5;
            } else if (s == "X") {
                return 10;
            } else if (s == "L") {
                return 50;
            } else if (s == "C") {
                return 100;
            } else if (s == "D") {
                return 500;
            } else {
                return 1000;
            }
        } else {
            int sum = 0;

            for (int i = 0; i < s.length(); ++i) {
                const string ch = s.substr(i, 1);

                if (i != s.length() - 1) {
                    const string nextCh = s.substr(i+1, 1);

                    if (ch == "I") {
                        if (nextCh == "V") {
                            sum += 4;
                            ++i;
                        } else if (nextCh == "X") {
                            sum += 9;
                            ++i;
                        } else {
                            sum += romanToInt(ch);
                        }
                    } else if (ch == "X") {
                        if (nextCh == "L") {
                            sum += 40;
                            ++i;
                        } else if (nextCh == "C") {
                            sum += 90;
                            ++i;
                        } else {
                            sum += romanToInt(ch);
                        }
                    } else if (ch == "C") {
                        if (nextCh == "D") {
                            sum += 400;
                            ++i;
                        } else if (nextCh == "M") {
                            sum += 900;
                            ++i;
                        } else {
                            sum += romanToInt(ch);
                        }
                    } else {
                        sum += romanToInt(ch);
                    }
                } else {
                    sum += romanToInt(ch);
                }
            }

            return sum;
        } 
    }
};