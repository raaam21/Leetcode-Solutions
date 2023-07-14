# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans=0

        # check notes here

        def target_parent(node,target):
            if node is None:
                return
            if node.val==target:
                nonlocal ans
                ans+=1
            
            target_parent(node.left,target-node.val)
            target_parent(node.right,target-node.val)

        def target_from_here(node,target):
            if node is None:
                return
            if node.val==target:
                nonlocal ans
                ans+=1
            
            target_from_here(node.left,targetSum)
            target_from_here(node.right,targetSum)
            
            target_parent(node.left,target-node.val)
            target_parent(node.right,target-node.val)

        target_from_here(root,targetSum)
        
        return ans
            

