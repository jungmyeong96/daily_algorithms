#Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
import numpy as np
from collections import Counter
from typing import List
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    #1. value값 기준으로 정렬하고 np함수로 split
    # frequency = Counter(nums)
    # frequency_sorted = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    # #frequency_sorted = {k: v for k, v in sorted(frequency.items(), key=lambda x: x[1], reverse=True)}
    # return np.split(list(frequency_sorted.keys()), [k])[0]

    #2. 우선순위 큐를 사용한 해법
    # frequency = Counter(nums)

    # freq_heap = []
    # #힙에 밸류와 키의 위치를 바꾼 뒤, 키를 음수로 삽입
    # for f in frequency:
    #     heapq.heappush(freq_heap, (-frequency[f], f))

    # topk = list()
    # for _ in range(k):
    #     topk.append(heapq.heappop(freq_heap)[1])
    # return topk

    #3. 파이썬스러운 방식
    return list(zip(*Counter(nums).most_common(k)))[0]
    #ZIP: 튜플을 인덱스에 따라 묶어주는 함수 zip((1, 3), (2, 2)) => (1, 2), (3, 2)
    #*: unpaking 리스트나 튜플을 벗겨낸다.
    #*: 반대로 패킹도 가능  print("1", "2")와 같은 원리 => 1, 2
    #a, *b = [1, 2, 3, 4] => a = 1,  b = [2, 3, 4]
    #**: key/value페어도 언패킹 가능
print(topKFrequent([1,1,1,3,3,2], 2))