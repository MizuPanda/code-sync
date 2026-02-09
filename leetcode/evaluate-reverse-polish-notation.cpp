class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (int i = 0; i < tokens.size(); ++i) {
          
            const string token = tokens.at(i);

            if (token == "+" || token == "-" || token == "*" || token == "/") {
                const int second = st.top();
                st.pop();

                const int first = st.top();
                st.pop();  

                if (token == "+") {
                    st.push(first + second);
                } else if (token == "-") {
                    st.push(first - second);
                } else if (token == "*") {
                    st.push(first*second);
                } else if (token == "/") {
                    st.push(first/second);
                }
            } else {
                st.push(stoi(token));
            }
            
        }

        return st.top();
    }
};