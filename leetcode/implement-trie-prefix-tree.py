class Trie {
private:
    vector<unique_ptr<Trie>> children;

    int pos(const char c) const {
        if (c == '$') return 26;

        return c - 'a';
    } 

public:
    Trie() {
        for (int i = 0; i < 27; ++i) {
            children.emplace_back(nullptr);
        }
    }
    
    void insert(string word) {
        word += "$";

        Trie* t = this;

        for (int i = 0; i < word.length(); ++i) {
            const int p  = pos(word.at(i));

            if (t->children.at(p) == nullptr) {
                t->children.at(p) = make_unique<Trie>();
            } 

            t = t->children.at(p).get();
        }
    }
    
    bool search(string word) {
        word += "$";

        Trie* t = this;

        for (int i = 0; i < word.length(); ++i) {
            const char c = word.at(i);
            const int p = pos(c);

            if (t->children.at(p) == nullptr) {
                return false;
            } else if (c == '$') {
                return true;
            }  else {
                t = t->children.at(p).get();
            }
        }

        return false;
    }
    
    bool startsWith(string prefix) {
        Trie* t = this;

        for (int i = 0; i < prefix.length(); ++i) {
            const int p = pos(prefix.at(i));

            if (t->children.at(p) == nullptr) {
                return false;
            } else {
                t = t->children.at(p).get();
            }
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */