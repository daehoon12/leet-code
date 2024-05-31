class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val counts: MutableMap<String, Int> = mutableMapOf()
        
        val words = paragraph.replace(Regex("\\W+"), " ").toLowerCase().split(" ").filter { it !in banned && it.isNotEmpty() }   
        
        for (word in words){
            counts[word] = counts.getOrDefault(word, 0) + 1
        }

        return counts.maxBy {it.value}!!.key
    }
}