from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people = sorted(people, key=lambda x:(-x[1], x[0]))
            
        # result = []
        # for i in range(len(people)):
        #     h, k = people[i]
        #     print(h,k)
        #     result.insert(k, [h, k])
        # return result
        heap = []
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))