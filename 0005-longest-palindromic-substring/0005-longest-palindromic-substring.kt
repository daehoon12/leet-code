class Solution {
    fun longestPalindrome(s: String): String {
        var left = 0
        var maxLen = 0
        val len = s.length
        fun check(start: Int, end: Int){
            var i = start
            var j = end
            while (i >= 0 && j < len && s[i] == s[j]){
                i--
                j++
            }

            if (j - i -1 > maxLen){
                maxLen = j - i -1
                left = i + 1
            }
        }

        if (len < 2){
            return s
        }
        for (i in 0 until len){
            check(i, i+1)
            check(i, i+2)
        }

        return s.substring(left, left + maxLen)
    }
}