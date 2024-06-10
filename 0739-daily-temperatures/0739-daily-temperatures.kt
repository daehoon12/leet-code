import java.util.Deque
import java.util.ArrayDeque

class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        val answer = IntArray(temperatures.size)
        val stack = ArrayDeque<Int>()
        
        for (i in 0 until temperatures.size){
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                val last = stack.pop()
                answer[last] = i - last
            }
            stack.push(i)
        }
        return answer
    }
}