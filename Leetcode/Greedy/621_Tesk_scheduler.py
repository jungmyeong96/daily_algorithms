class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_result = 0
            for task, _ in counter.most_common(n + 1):
                sub_result += 1
                result += 1

                counter.subtract(task)
                # 0이하 생략
                counter += collections.Counter()

            if not counter:
                break
            
            #idle 계산
            result += n - sub_result + 1
        return result


tasks = ["A","A","A","B","B","B"]
n = 2

print(Solution().leastInterval(tasks, n))