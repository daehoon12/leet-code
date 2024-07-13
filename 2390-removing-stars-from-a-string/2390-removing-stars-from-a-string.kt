class Solution {
    fun removeStars(s: String): String {
          val deque = ArrayDeque<Char>()
          
          for (i in s.indices){
              if (deque.isEmpty()){
                  deque.add(s[i])
              } else if (deque.isNotEmpty() && s[i] == '*'){
                deque.removeLast()
                } else{
                    deque.add(s[i])
              }
          }
        return deque.joinToString("")
    }
}