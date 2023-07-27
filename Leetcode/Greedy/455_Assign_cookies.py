class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # child = []
        # cookies = []
        # for i in range(len(g)):
        #     heapq.heappush(child, -g[i])
        # for i in range(len(s)):
        #     heapq.heappush(cookies, -s[i])
   
        # result = 0
        # cookie_i = 0
        # for i in range(len(child)):
        #     if not cookies:
        #         break
        #     chi = heapq.heappop(child)
        #     coo = heapq.heappop(cookies)
        #     if (-chi <= -coo):
        #         result += 1
        #     else:
        #         heapq.heappush(cookies, coo)
        # return result
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i
