import collections;
import re;
from typing import List;

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    
    # print(max(counts, key=counts.get))

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))