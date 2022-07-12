from re import I
from typing import List

class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index:]
            if j in temp_nums:
                return [start_index, next_index + temp_nums.index(j)]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum_2([2, 7, 11, 15], 9))