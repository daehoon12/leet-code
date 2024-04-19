# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = 100000000
        def inorder(root):
            ret = []
            if root.left:
                ret += inorder(root.left)
            ret.append(root.val)
            if root.right:
                ret += inorder(root.right)
            return ret

        arr = inorder(root)
        for i in range(len(arr)-1):
            answer = min(answer, arr[i+1] - arr[i])
        return answer