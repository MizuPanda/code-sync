/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
private:
    // Input: Random Node to be copied, and node map 
    Node* copyRandom(Node* node, unordered_map<Node*, Node*>& nodeMap) {
        return nodeMap[node];
    }

    Node* copyList(Node* node, unordered_map<Node*, Node*>& nodeMap) {
        if (node == nullptr) {
            return nullptr;
        }

        Node* n;

        n = new Node(node->val);

        nodeMap[node] = n;

        n->next = copyList(node->next, nodeMap);
        n->random = copyRandom(node->random, nodeMap);

        return n;
    }

public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> nodeMap;
        Node* node;

        node = copyList(head, nodeMap);

        return node;
    }
};