# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder는 root를 가장 먼저 방문함. 이 성질을 이용해서 inorder에 왼쪽, 오른쪽 node를 연결할 수 있음..!
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            curr = preorder.pop(0)
            idx = inorder.index(curr)
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])

            return node