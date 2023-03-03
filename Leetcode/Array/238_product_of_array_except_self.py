from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    ans = []
    # 나눗셈이 금지이므로 자신을 제외한 왼쪽 곱과 오른쪽곱을 따로 구한 뒤, 다 같이 곱한다
    p = 1
    #왼쪽 곱
    #1, 1, 2, 6
    for i in range(len(nums)):
        ans.append(p)
        p = p * nums[i]
    
    p = 1
    #오른쪽 곱
    #24 12 4 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] = ans[i] * p
        p = p * nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))