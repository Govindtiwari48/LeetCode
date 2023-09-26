# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,ans):
        if root==None:
            return 0
        l=self.helper(root.left,ans)
        r= self.helper(root.right,ans)
        ans[0]+=abs(l-r)
        return root.val+l+r
        

    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        self.helper(root,ans)
        return ans[0]