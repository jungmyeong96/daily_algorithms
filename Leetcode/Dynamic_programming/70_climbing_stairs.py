class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        # steps = []
        # steps.append(1)
        # for i in range(1, n + 1):
        #     if i - 2 >= 0:
        #         steps.append(steps[i - 1] + steps[i - 2])
        #     else:
        #         steps.append(steps[i - 1])
        # return steps[n]
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]
        