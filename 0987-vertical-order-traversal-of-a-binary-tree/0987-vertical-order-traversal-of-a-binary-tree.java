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

class Tuple{
    TreeNode node;
    int hd,level;
    Tuple(TreeNode node, int hd, int level){
        this.node = node;
        this.hd = hd;
        this.level = level;
    }
}

class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        TreeMap<Integer,TreeMap<Integer,PriorityQueue<Integer>>> map = new TreeMap<>();

        Queue<Tuple> q = new LinkedList<>();

        q.add(new Tuple(root,0,0));

        while(!q.isEmpty()){
            Tuple curr = q.poll();

            TreeNode node = curr.node;
            int hd = curr.hd;
            int level = curr.level;

            map.putIfAbsent(hd,new TreeMap<>());
            map.get(hd).putIfAbsent(level,new PriorityQueue<>());
            map.get(hd).get(level).offer(node.val);

            if(node.left != null){
                q.add(new Tuple(node.left,hd-1,level+1));
            }

            if(node.right != null){
                q.add(new Tuple(node.right,hd+1,level+1));
            }
        }

        List<List<Integer>> res = new ArrayList<>();

        for(TreeMap<Integer,PriorityQueue<Integer>> levels:map.values()){
            res.add(new ArrayList<>());
            for(PriorityQueue<Integer> nodes:levels.values()){
                while(!nodes.isEmpty()){
                    res.get(res.size()-1).add(nodes.poll());
                }
            }
        }

        return res;
    }
}