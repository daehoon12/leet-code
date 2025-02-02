class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        return ' '.join(list(filter(lambda x: x != '', words[::-1]))).strip()