class Solution {
    fun maxProfit(prices: IntArray): Int {
        var answer = 0
        var curr = prices[0]

        for (i in 1 until prices.size){
            when {
                curr > prices[i]  -> curr = prices[i]
                else -> answer = max(answer, (prices[i] - curr))
            }
        }
        return answer
    }
}