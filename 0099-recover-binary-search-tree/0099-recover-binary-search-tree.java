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
    public void recoverTree(TreeNode root) {
        ArrayList<TreeNode> arr = new ArrayList<>();

        inorder(root,arr);

        TreeNode node1 = null, node2 = null;
        for(int i=0;i<arr.size()-1;i++){
            if(arr.get(i).val>arr.get(i+1).val){
                node2 = arr.get(i+1);
                if(node1 == null){
                    node1 = arr.get(i);
                }
            }
        }

        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }

    private void inorder(TreeNode root,List<TreeNode> arr){
        if(root == null) return;

        inorder(root.left,arr);
        arr.add(root);
        inorder(root.right,arr);
    }
}