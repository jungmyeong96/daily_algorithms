# import sys

# def checkADM():
#     nums = list(map(int, sys.stdin.readline().strip().split()))
#     if nums[0] > nums[-1]:
#         for i in range(4):
#             if not (nums[i] > nums[i + 1] and nums[7 - i] < nums[7 - i - 1]):
#                 print("mixed")
#                 return
#         print("descending")
#     elif nums[0] < nums[-1]:
#         for i in range(4):
#             if not (nums[i] < nums[i + 1] and nums[7 - i] > nums[7 - i - 1]):
#                 print("mixed")
#                 return
#         print("ascending")

# checkADM()

import sys
input = sys.stdin.readline

numbers = list(map(int,input().split()))

if numbers == [1,2,3,4,5,6,7,8] :
    print("ascending")
elif numbers == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")