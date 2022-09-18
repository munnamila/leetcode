
class Solution:
    def search(self, nums, target):


        low, mid, high = 0, 0, len(nums)-1# 初期設定
    

        # lowとhighが解になるときの対応
        if nums[low] == target: return low
        elif nums[high] == target: return high


        while low <= high:
            mid = low + ((high-low)//2)# 中央indexの計算
            if nums[mid] == target: return mid# 中央値はtargetであるかどうかの判断
            elif nums[mid] > target: high = mid-1# targer>midの時
            else: low = mid+1# targer<midの時
        return -1# 探す値が存在しないとき


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))