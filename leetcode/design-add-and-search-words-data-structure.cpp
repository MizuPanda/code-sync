class WordDictionary {
private:
    unordered_map<char, unique_ptr<WordDictionary>> children;
    vector<char> present;
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        word += "$";

        WordDictionary* d = this;

        for (int i = 0; i < word.length(); ++i) {
            const char c = word.at(i);

            if (d->children.find(c) == d->children.end()) {
                string n{c};
                d->children[c] = make_unique<WordDictionary>();
                d->present.push_back(c);
            }

            d = d->children[c].get();
        }
    }
    
    bool search(string word) {
        word += "$";
        return searchHelper(word, this);
    }

    bool searchHelper(const string& word, WordDictionary* dict) {

        if (word.empty()) {
            return true;
        }

        const char c = word.at(0);

        if (c == '.') {
            bool found = false;

            for (int i = 0; i < dict->present.size() && !found; ++i) {
                found = searchHelper(word.substr(1), dict->children[dict->present.at(i)].get());
            }

            return found;
        } else if (dict->children.find(c) == dict->children.end()) {
            return false;
        }

        return searchHelper(word.substr(1), dict->children[c].get());
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */