from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solve(i : int):
            if i == n:
                ans.append("".join(tmp_ans))
                return
            
            for ch in myMap[digits[i]]:
                tmp_ans.append(ch)
                solve(i+1)
                tmp_ans.pop()
                

        if digits == None or len(digits) == 0:
            return []

        myMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        tmp_ans = []
        n = len(digits)
        solve(0)
        return ans

if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.letterCombinations("23"))