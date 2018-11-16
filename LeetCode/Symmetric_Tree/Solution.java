class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x){
        val = x;
    }
}

public class Solution {
    public boolean isSymmetric(TreeNode root) {
        return scene(root.left, root.right);
    }

    private boolean scene(TreeNode left, TreeNode right){
        if (left == null && right == null)
            return true;
        if (left == null || right == null)
            return false;

        return (left.val == right.val)
                && (scene(left.left, right.right))
                && (scene(left.right, right.left));
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);

        root.right = new TreeNode(2);
        root.right.right = new TreeNode(3);
        root.right.left = new TreeNode(4);

        Solution s = new Solution();
        System.out.println(s.isSymmetric(root));
    }
}