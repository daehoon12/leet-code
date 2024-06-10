class Solution {
    fun trap(height: IntArray): Int {
        var left = 0
        var right = height.size -1
        
        var leftMax = height[left]
        var rightMax = height[right]

        var answer = 0
        while (left < right){
            when {
                leftMax < rightMax -> {
                    answer += leftMax - height[left]
                    left++
                    leftMax = max(leftMax, height[left])
                }
                else -> {
                    answer += rightMax - height[right]
                    right--
                    rightMax = max(rightMax, height[right])
                }
            }
        }
        return answer
    }
}