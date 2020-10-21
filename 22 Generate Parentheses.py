from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(i : int, leftCnt : int, allLeftCnt):
            if i == 2*n:
                ans.append("".join(tmp_ans))
                return
            
            if allLeftCnt < n:
                tmp_ans.append('(')
                backtrack(i+1, leftCnt+1, allLeftCnt+1)
                tmp_ans.pop()
            if leftCnt > 0:
                tmp_ans.append(')')
                backtrack(i+1,leftCnt-1,allLeftCnt)
                tmp_ans.pop()
               

        ans = []
        tmp_ans = []
        backtrack(0,0,0)
        return ans

if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.generateParenthesis(3))