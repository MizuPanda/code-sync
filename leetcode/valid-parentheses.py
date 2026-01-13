class Solution {
public:
    bool isValid(string s) {
        stack<string> st;

        for (int i = 0; i < s.length(); ++i) {
            const string c = s.substr(i, 1);

            if (c == "(" || c == "{" || c == "[") {
                st.push(c);
            } else if (!st.empty() && 
                      ((c == ")" && st.top() == "(") || 
                       (c == "]" && st.top() == "[") ||
                       (c == "}" && st.top() == "{"))) {

                st.pop();
            } else {
                return false;
            }
        }

        return st.empty();
    }
};