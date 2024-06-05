class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        answer = 0
        left_max = height[left]
        right_max = height[right]
    
        while left < right:
            if left_max < right_max:
                answer += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                answer += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
                
        return answer
            
            
            
