#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };


class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        iter(root);
        sort(vals.begin(), vals.end());
        int minDiff = INT_MAX;
        for (int i = 1; i < vals.size(); ++i)
            minDiff = min(minDiff, vals.at(i) - vals.at(i-1));
        return minDiff;
    }

private:
    vector<int> vals;
    void iter(TreeNode* node){
        if (node == nullptr) return;
        vals.push_back(node->val);
        iter(node->left);
        iter(node->right);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    TreeNode root(4);
    root.left = new TreeNode(2);
    root.right = new TreeNode(6);
    root.left->left = new TreeNode(1);
    root.left->right = new TreeNode(3);

    int result = s.minDiffInBST(&root);
    cout << result << endl;
    return 0;
}