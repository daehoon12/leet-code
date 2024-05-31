import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = filter(lambda x: (x not in banned), re.sub(r'[^\w]', ' ', paragraph).lower().split())
        return Counter(paragraph).most_common(1)[0][0]