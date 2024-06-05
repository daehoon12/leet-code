class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        val answer = mutableSetOf<List<Int>>()
        nums.sort()
        
        for (i in nums.indices) {
            var low = i + 1
            var high = nums.size - 1
            
            while (low < high) {
                val sum = nums[i] + nums[low] + nums[high]
                
                when {
                    sum == 0 -> {
                        answer.add(listOf(nums[i], nums[low], nums[high]))
                        low++
                        high--
                    }
                    sum > 0 -> high--
                    else -> low++
                }
            }
        }
        
        return answer.toList()
    }
}
