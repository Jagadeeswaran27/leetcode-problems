/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> arr = new ArrayList<>();

        dfs(root,0,arr);

        return arr;
    }

    private void dfs(TreeNode root, int level, List<Integer> arr){
        if(root == null) return;

        if(level == arr.size()){
            arr.add(root.val);
        }

        dfs(root.right,level+1,arr);
        dfs(root.left,level+1,arr);
    }
}