class Solution {
    fun longestPalindrome(s: String): String {
        var left = 0
        var maxLen = 0
        
        fun extend(low: Int, high: Int){
            var i = low
            var j = high

            while (i >=0 && j < s.length && s[i] == s[j]){
                i--
                j++
            }

            if (maxLen < j - i -1){
                maxLen = j - i -1
                left = i + 1
            }
        }

        if (s.length < 2){
            return s
        }

        for (i in 0 until s.length -1){
            extend(i, i + 1)
            extend(i, i + 2)
        }

        return s.substring(left, left + maxLen)
    }
}