from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        # # nums = [2,7,11,15]

        # # construct the map
        # n = len(nums)
        # for i in range(n):
        #     numMap[nums[i]] = i

        # # create compliment and check if it exists in numMap
        # for i in range(n):
        #     compliment = target - nums[i]
        #     if compliment in numMap:
        #         return [numMap[compliment], i]

        # return []

        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found