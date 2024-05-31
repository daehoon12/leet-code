class Solution:
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1

        while low < high:
            if not s[low].isalpha():
                low +=1
            elif not s[high].isalpha():
                high -=1
            else:
                if s[low].lower() != s[high].lower():
                    return False
                low += 1
                high -= 1
        return True