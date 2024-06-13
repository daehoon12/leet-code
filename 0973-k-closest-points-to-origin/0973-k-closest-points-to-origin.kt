class Solution {
    data class Point(
        var distance: Long,
        var point: IntArray
    )

    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        val answer = mutableListOf<IntArray>()
        val pq = PriorityQueue<Point>(compareBy { x -> x.distance})

        for (point in points){
            pq.add(Point(point[0].toLong() * point[0] + point[1].toLong() * point[1], point))            
        }
        var count = k
        while (count > 0) {
            answer.add(pq.poll().point)
            count--
        }
        return answer.toTypedArray()
    }
}