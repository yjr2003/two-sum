from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in index:
            return [index[num2], i]
        index[num] = i
    return []
