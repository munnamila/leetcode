from re import I
from typing import List

class Solution:

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        # 1 arrayを繰り返し
        # 2 該当する値とtargetの差を計算
        # 3 残りの値の中にこの差があるかどうかを調査
        for i in nums:
            j = target - i # 当一个数位i时，另个数应该为j
            start_index = nums.index(i)# i的索引
            next_index = nums.index(i) + 1# i的下个数的索引
            if j in nums[next_index:]:
                return [start_index, next_index + nums[next_index:].index(j)]


    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        # use hash tabel(python: dicrionary)
        dict = {}
        for i  in range(len(nums)):
            # 遍历nums的index
            j = target - nums[i]# 当一个数位i时，另个数应该为j

            if j not in dict:
                # 如果j不在dict的key里

                # 保存i为key，其索引为value
                dict[nums[i]] = i

            else:
                # 否则返回字典里key为j的value，和i
                return [dict[j], i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum_1([2, 7, 11, 15], 13))
    print(solution.twoSum_2([2, 7, 11, 15], 13))