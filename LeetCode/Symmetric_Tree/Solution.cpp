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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return scene(root->left, root->right);
    }

private:
    bool scene(TreeNode* left, TreeNode* right){
        if (left == 0 && right == 0)
            return true;
        if (left == 0 || right == 0)
            return false;

        return (left->val == right->val) &&
                scene(left->left, right->right) &&
                scene(left->right, right->left);
    }
};

int main(int argc, char const *argv[])
{
    TreeNode root = TreeNode(1);
    TreeNode left = TreeNode(2);
    TreeNode right = TreeNode(2);
    root.left = &left;
    root.right = &right;

    TreeNode leftLeft = TreeNode(3);
    TreeNode leftRight = TreeNode(4);
    TreeNode rightLeft = TreeNode(4);
    TreeNode rightRight = TreeNode(3);

    root.left->left = &leftLeft;
    root.left->right = &leftRight;
    root.right->left = &rightLeft;
    //root.right->right = &rightRight;

    Solution s;
    cout << s.isSymmetric(&root) << endl;
    return 0;
}