from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 0:
            return []
        if target == 0:
            return [[]]

        def dfs(curIndex : int, curSum : int, tmp_ans : List[int]):
            if curSum > target:
                return
            if curSum == target:
                ans.append(tmp_ans.copy())
                return
            if curIndex >= arr_len:
                return

            tmp_sum = curSum
            for i in range(0, target // candidates[curIndex] + 1):
                dfs(curIndex+1, tmp_sum, tmp_ans)
                tmp_ans.append(candidates[curIndex])
                tmp_sum += candidates[curIndex]
            
            for i in range(0, target // candidates[curIndex] + 1):
                tmp_ans.pop()
            
        arr_len = len(candidates)
        ans = []
        tmp_ans = []
        dfs(0, 0, tmp_ans)
        return ans
        


if __name__ == "__main__":
    solveObj = Solution()
    print(solveObj.combinationSum([2,3,5],8))