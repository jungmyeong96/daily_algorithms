from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    #브루트 포스를 사용하면 O(n^3)로 타임아웃
    #정렬된 배열을 투포인터기법으로 해결
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        #중복된 값은 배제
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        #i의 우측에 있는 나머지 값들의 간격을 좁혀가면서 Sum을 판단
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                
                #동일한 값을가진 left와 right배제
                while left < right and nums[left] ==  nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results
        
print(threeSum([-1,0,1,2,-1,-4]))