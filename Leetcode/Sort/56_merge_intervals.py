from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x : x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(i[1], merged[-1][1])
            else:
                merged.append(i)
                #merged += i,
        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(Solution().merge(intervals))