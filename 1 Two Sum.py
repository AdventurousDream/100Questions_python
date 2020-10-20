from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for index,val in enumerate(nums):
            if (target - val) in mymap:
                return [mymap.get(target - val), index]
            mymap[val] = index;


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums,target))
