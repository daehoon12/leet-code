class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val answer = mutableListOf<List<Int>>()

        fun dfs(idx: Int, tmp: MutableList<Int>){
            if (tmp.size == k){
                answer.add(tmp.toList())
                return
            }

            for (i in idx until n+1){
                tmp.add(i)
                dfs(i+1, tmp)
                tmp.removeAt(tmp.size - 1)
            }   
        }
        
        dfs(1, mutableListOf())
        return answer
    }
}