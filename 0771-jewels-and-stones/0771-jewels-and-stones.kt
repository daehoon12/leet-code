class Solution {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        var answer = 0
        val jewelsSet = jewels.toSet()

        for (stone in stones) {
            if (jewelsSet.contains(stone)) {
                answer += 1
            }
        }
        return answer
    }
}
