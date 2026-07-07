class Twitter {
private:
    int count = 0;
    unordered_map<int, unordered_set<int>> userFollowers;
    unordered_map<int, vector<pair<int, int>>> tweetMap;

    struct Tweet {
        int count;
        int tweetId;
        int userId;
        int index;
    };

    struct TweetComparator {
        bool operator()(const Tweet& a, const Tweet& b) {
            return a.count < b.count;
        }
    };
public:
    Twitter() {
        
    }
    
    void postTweet(int userId, int tweetId) {
        
        if (tweetMap.find(userId) == tweetMap.end()) {
            tweetMap[userId] = {};
        }

        tweetMap[userId].push_back({count, tweetId});
        ++count;

    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> res;

        priority_queue<Tweet, vector<Tweet>, TweetComparator> maxHeap;

        if (tweetMap.find(userId) != tweetMap.end()) {
            int index = tweetMap[userId].size() - 1;
            pair<int, int> tweet = tweetMap[userId].at(index);
            maxHeap.push({tweet.first, tweet.second, userId, index});
        }

        for (int followeeId : userFollowers[userId]) {
            if (tweetMap.find(followeeId) != tweetMap.end()) {
                int index = tweetMap[followeeId].size() - 1;
                pair<int, int> tweet = tweetMap[followeeId].at(index);
                maxHeap.push({tweet.first, tweet.second, followeeId, index});
            }
        }

        while (!maxHeap.empty() && res.size() < 10) {
            Tweet topTweet = maxHeap.top();
            res.emplace_back(topTweet.tweetId);
            maxHeap.pop();

            if (topTweet.index > 0) {
                pair<int, int> tweet = tweetMap[topTweet.userId].at(topTweet.index - 1);
                maxHeap.push({tweet.first, tweet.second, topTweet.userId, topTweet.index - 1});
            }
        }

        return res;
    }
    
    void follow(int followerId, int followeeId) {

        if (userFollowers.find(followerId) == userFollowers.end()) {
            userFollowers[followerId] = {};
        }
        
        userFollowers[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (userFollowers.find(followerId) != userFollowers.end() && userFollowers[followerId].find(followeeId) != userFollowers[followerId].end()) {
            userFollowers[followerId].erase(followeeId);
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */