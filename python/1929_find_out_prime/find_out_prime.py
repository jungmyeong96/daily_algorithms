# import time
import math

# start = time.time()
M, N = map(int, input().split())
# # arr = [True for x in range(1000001)]
# check = True
# # arr[1] = False
# for target in range(M, N + 1):
#     if target == 1:
#         continue
#     for idx in range(2, int(math.sqrt(target)) + 1):
#         if (target % idx == 0):
#             check = False
#             # arr[target] = False
#             break
#     if check:
#         print(target)
#     check = True

# # for i in range(M, N + 1):
# #     if arr[i]:
# #         print(i)

# end = time.time()

# print(f"{end - start:.5f} sec")



arr = [True for x in range(1000001)]
arr[1] = False
for target in range(2, int(math.sqrt(N)) + 1):
    if arr[target]:
        idx = 2
        while target * idx <= N:
            arr[target * idx] = False
            idx += 1

for i in range(M, N + 1):
    if arr[i]:
        print(i)
