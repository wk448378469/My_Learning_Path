class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        self.iter(root)
        self.vals.sort()
        minDiff = float('inf')
        for i in range(1, len(self.vals)):
            if self.vals[i] - self.vals[i-1] < minDiff:
                minDiff = self.vals[i] - self.vals[i-1]

        return minDiff

    def iter(self, node):
        if node is None: return
        self.vals.append(node.val)
        self.iter(node.left)
        self.iter(node.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    result = s.minDiffInBST(root)
    print(result)
