class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target = strs[0]
        index = 987654321
        for s in strs:
            curr = 0
            for i in range(min(len(s), len(target))):
                if s[i] == target[i]:
                    curr += 1
                else:
                    break
            index = min(index, curr)
        return "".join(target[:index])