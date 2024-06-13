class Solution {
    fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
        val pq = PriorityQueue<Int>()       
        var answer = heights.size -1
        var totalBricks = bricks
        for (i in 1 until heights.size){
            if (heights[i] -heights[i-1] > 0){
                pq.add(heights[i] -heights[i-1])
            }
            
            if (pq.size > ladders){
                val usedBrick = pq.poll()
                if (totalBricks - usedBrick < 0){
                    answer = i - 1
                    break
                }
                totalBricks -= usedBrick
            }
        }

        return answer
    }
}