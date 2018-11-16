# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.scene(root.left, root.right)

    def scene(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return (left.val == right.val) and  \
               (self.scene(left.left, right.right))and  \
               (self.scene(left.right, right.left))


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    s = Solution()
    print(s.isSymmetric(root))
