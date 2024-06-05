class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        answer = 0
        low, high = 0, n -1
        max_left, max_right = height[low], height[high]
        while low < high:
            
            if height[low] < height[high]:
                answer += max_left - height[low]
                low += 1
            else:
                answer += max_right - height[high]
                high -= 1
            max_left = max(max_left, height[low])
            max_right = max(max_right, height[high])
        return answer
                