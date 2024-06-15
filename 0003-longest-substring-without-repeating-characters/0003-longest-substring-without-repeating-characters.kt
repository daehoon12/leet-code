import java.util.HashMap

class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val sLen = s.length
        if (sLen == 0) {
            return 0
        }
        val dic = HashMap<Char, Int>()
        var left = 0
        var right = 0
        var answer = 0

        while (right < sLen) {
            when {
                !dic.containsKey(s[right]) || dic[s[right]] == 0 -> {
                    dic[s[right]] = dic.getOrDefault(s[right], 0) + 1
                    right++
                }
                else -> {
                    dic[s[left]] = dic.getOrDefault(s[left], 0) - 1
                    left++
                }
            }
            answer = maxOf(answer, right - left)
        }
        return answer
    }
}
