from collections import Counter
import sys

count = int(sys.stdin.readline())
num_arr = []

for _ in range(count):
    num = int(sys.stdin.readline()) #int(input())보다 빠름
    num_arr.append(num)

num_arr.sort()


print(round(sum(num_arr) / count))
print(num_arr[count // 2])

cnt = Counter(num_arr).most_common(2)

if count > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(num_arr[-1] - num_arr[0])
