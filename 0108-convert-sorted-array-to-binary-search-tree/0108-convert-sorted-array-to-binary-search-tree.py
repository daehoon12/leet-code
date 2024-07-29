# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary_search(low, high):
            if low > high:
                return None
            mid = low + (high - low) // 2
            
            node = TreeNode(nums[mid])
            node.left = binary_search(low, mid - 1)
            node.right = binary_search(mid + 1, high)
            
            return node

        if len(nums) == 0:
            return None
        return binary_search(0, len(nums)-1)

    