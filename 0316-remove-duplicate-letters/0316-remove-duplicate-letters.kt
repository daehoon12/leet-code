import java.util.ArrayDeque; 


class Solution {
    fun removeDuplicateLetters(s: String): String {
        val count = mutableMapOf<Char, Int>()
        val seen = mutableMapOf<Char, Boolean>()
        val stack = ArrayDeque<Char>()

        for (ch in s){
            count[ch] = count.getOrDefault(ch, 0) + 1
        }


        for (ch in s){
            count[ch] = count[ch]!! - 1

            if (seen[ch] == true)
                continue
        
            while (stack.isNotEmpty() && stack.peek() > ch && count[stack.peek()]!! > 0){
                seen[stack.pop()] = false
            }
            stack.push(ch)
            seen[ch] = true
        }

        val sb = StringBuilder()

        while (stack.isNotEmpty()){
            sb.append(stack.pollLast())
        }

        return sb.toString()
    }
}