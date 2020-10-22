from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr_len = len(nums)
        if arr_len == 0:
            return [-1, -1]
        if arr_len == 1:
            if target == nums[0]:
                return [0, 0]
            else:
                return [-1, -1]
        
        l, r = 0, arr_len - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l >= arr_len or nums[l] != target:
            return [-1, -1]
        left_index = l

        l, r = 0, arr_len - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        right_index = l
        if l >= arr_len or nums[l] != target:
            right_index -= 1

        return [left_index, right_index]


if __name__ == "__main__":
    solveObj = Solution()
    print(solveObj.searchRange([2,2], 2))