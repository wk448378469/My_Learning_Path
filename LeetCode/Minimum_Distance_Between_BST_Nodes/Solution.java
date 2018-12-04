import java.util.Collections;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    List<Integer> vals = new ArrayList<Integer>();

    public int minDiffInBST(TreeNode root) {
        iter(root);
        Collections.sort(vals);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 1; i < vals.size(); i++) {
            if (vals.get(i) - vals.get(i-1) < minDiff)
                minDiff = vals.get(i) - vals.get(i-1);
        }
        return minDiff;
    }

    private void iter(TreeNode node){
        if (node == null) return;
        vals.add(node.val);
        iter(node.left);
        iter(node.right);
    }
}