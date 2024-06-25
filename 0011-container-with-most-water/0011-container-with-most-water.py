class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height)-1
        answer = 0
        while low < high:
            curr_height = 0
            if height[low] <= height[high]:
                curr_height = height[low]
                answer = max(answer, (high - low) * curr_height)
                low +=1
            else:
                curr_height = height[high]
                answer = max(answer, (high - low) * curr_height)
                high -= 1

        return answer