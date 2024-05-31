class Solution {
    fun reverseString(s: CharArray): Unit {
        var low = 0
        var high = s.size -1
        
        while (low < high){
            s[low] = s[high].also {s[high] = s[low]}
            low++
            high--
        }

    }
}