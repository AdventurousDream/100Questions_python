from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr_len = len(nums)
        if arr_len == 0:
            return 1
        if arr_len == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        
        i = 0
        while i < arr_len:
            if nums[i] <= 0 or nums[i] > arr_len:
                nums[i] = -1
            elif nums[i] == i + 1:
                pass
            elif nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i],nums[tmp-1] = nums[tmp-1],nums[i]
                i -= 1
            else:
                nums[i] = -1
            i += 1

        for i in range(arr_len):
            if nums[i] != i+1:
                return i+1
        return arr_len+1


if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.firstMissingPositive([7,8,9,10,11,12]))