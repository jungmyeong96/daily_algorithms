from typing import List
from collections import deque

# def trap(height: List[int]) -> int:
#     checkWater = deque()
#     water = 0

#     for h in height:
#         checkWater.append(h)
#         if checkWater[0] == 0:
#             checkWater.popleft()
#             continue
#         if len(checkWater) > 1 and checkWater[-1] >= checkWater[0]:
#             if len(checkWater) == 2:
#                 checkWater.popleft()
#                 continue
#             minHeight = min(checkWater[-1],checkWater[0])
#             elevation = len(checkWater) * minHeight
#             blocks = 0
#             for block in checkWater:
#                 if minHeight < block:
#                     blocks += minHeight
#                 else: 
#                     blocks += block
#             print(checkWater)
#             for i in range(len(checkWater)):                   
#                 if len(checkWater) != 1:
#                     checkWater.popleft()
#             print(elevation, blocks, checkWater, elevation - blocks)
#             water += elevation - blocks
#     return water


# 투포인터를 사용하여 최대의 높이로 향하는 로직 구현
# Runtime 123 ms

# def trap(height: List[int]) -> int:
#     if not height:
#         return 0
#     volume = 0
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]

#     while left < right:
#         left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
#         if left_max <= right_max:
#             volume += left_max - height[left]
#             left += 1
#         else:
#             volume += right_max - height[right]
#             right -= 1
#     return volume


# 스택을 사용하여 변곡점을 찾아 물웅덩이 구하기
# Runtime 130 ms

def trap(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        #변곡점
        while stack and height[i] > height[stack[-1]]:
            print(stack)
            top = stack.pop()
            if not len(stack):
                break

            # 이전과의 차이만큼 물높이 처리
            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            
            volume += distance * water
        stack.append(i)
    return volume
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))