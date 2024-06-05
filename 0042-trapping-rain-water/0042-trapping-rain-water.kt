class Solution {
    fun trap(height: IntArray): Int {
        var left = 0
        var right = height.size -1
        var maxLeft = height[left]
        var maxRight = height[right]
        var answer = 0
        while (left < right){
            if (maxLeft < maxRight){
                answer += maxLeft - height[left] 
                left++
            } else{
                answer += maxRight - height[right]
                right--
            }
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
        }
        
        return answer
    }
}