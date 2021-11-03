from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
    
        def isValidBSTmm(root: Optional[TreeNode]) -> [bool,int,int]:
            if ((not root.right) and (not root.left)):
                return [True, root.val,root.val]
            if (root.left):
                if (root.left.val >= root.val):
                    return[False,0,0]                    
                [statl, leftmaxl,leftminr] = isValidBSTmm(root.left)
                statl = statl and max(leftmaxl,leftminr) < root.val
            if (root.right):
                if (root.right.val <= root.val):
                    return [False,0,0]
                [statr, rightmaxl,rightminr] = isValidBSTmm(root.right)                
                statr = statr and min(rightminr,rightmaxl) > root.val
            if (not root.right):
                return [statl,leftmaxl,root.val]
            if (not root.left):
                return [statr,root.val,rightminr]
            return [statl and statr,leftmaxl,rightminr]
        
        [ans,maxl,minr] = isValidBSTmm(root)
        return ans  
        
print(Solution().isValidBST(TreeNode(5,TreeNode(4),TreeNode(6,None,TreeNode(3)))))