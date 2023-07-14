# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        hm=defaultdict(list)
        def dfs(root,r,c):
            if root is None:
                return
            
            hm[c].append([r,root.val])
            dfs(root.left,r+1,c-1)
            dfs(root.right,r+1,c+1)
        
        dfs(root,0,0)
        print(hm)

        # conquoring the question
        # hm2=defaultdict(list)
        # for k,l in hm.items():
        #     hm2[k[1]].extend(l)
        # print(hm2)
        
        ans=[]
        while(len(hm)>0):
            x=min(hm.keys())
            hm[x].sort()
            t=[]
            for a,b in hm[x]:
                t.append(b)
            ans.append(t)
            del hm[x]
        return ans

