# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# stack = [left,right], stack is used FILO, so i append right first
# stack = [right,left]
# res = [root]
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.right != None:
                stack.append(root.right)
            if root.left != None:
                stack.append(root.left)

        return res
                

            
        