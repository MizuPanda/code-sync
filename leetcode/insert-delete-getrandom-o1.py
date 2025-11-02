class RandomizedSet {
    class Data {
        bool present;
        int pos;

        public:
            Data(const bool present, const int pos) : present{present}, pos {pos} {}
            Data() : present {false}, pos {-1} {}

            bool getPresent() {
                return present;
            }

            void setPresent(const bool present) {
                this->present = present;
            }

            int getPos() {
                return pos;
            }

            void setPos(const int pos) {
                this->pos = pos;
            }
    };

    unordered_map<int, Data> data;
    vector<int> values;

    bool isPresent(int val) {
        return data.find(val) != data.end() && data[val].getPresent();
    }

public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (!isPresent(val)) {
            data[val] = Data(true, values.size());
            values.emplace_back(val);
            return true;
        }

        return false;
    }
    
    bool remove(int val) {
        if (isPresent(val)) {
            data[val].setPresent(false);
    
            const int lastElement = values.at(values.size() - 1);
            
            if (val != lastElement) {
                const int pos = data[val].getPos();
                values.at(pos) = lastElement;
                data[lastElement].setPos(pos);            
            }

            values.pop_back();
            
            return true;
        }

        return false;
    }
    
    int getRandom() {
        const int randomNum = rand() % values.size();

        return values.at(randomNum);
    }
};