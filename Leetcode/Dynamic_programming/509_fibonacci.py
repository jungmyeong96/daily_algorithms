class Solution:
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        nums = []
        #부르트 포스
        # if n <= 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        #다이나믹프로그래밍
        # 타뷸레이션 상향식
        if n <= 1:
            return n
        nums.append(0)
        nums.append(1)
        for i in range(2, n + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n]

        #메모이제이션 하향식
        # if n <= 1:
        #     return n
        
        # if self.dp[n]:
        #     return self.dp[n]
        # self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        # return self.dp[n]
