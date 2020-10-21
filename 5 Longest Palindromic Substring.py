from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromeFromCenter(l : int, r : int) -> List[int]:
            error_flag = False
            while l >= 0 and r < s_len:
                if s[l] == s[r]:
                    l = l - 1
                    r = r + 1
                else:
                    error_flag = True
                    break
            if l < 0 or r >= s_len or error_flag:
                l += 1
                r -= 1
            return [r - l + 1, l ,r]
        
        s_len = len(s)
        res, final_l, final_r = 0, 0, 0
        for i in range(s_len):
            tmp_len, tmp_l, tmp_r = longestPalindromeFromCenter(i,i)
            if tmp_len > res:
                res, final_l, final_r = tmp_len, tmp_l, tmp_r
        for i in range(s_len - 1):
            tmp_len, tmp_l, tmp_r = longestPalindromeFromCenter(i,i+1)
            if tmp_len > res:
                res, final_l, final_r = tmp_len, tmp_l, tmp_r
        return s[final_l : final_r + 1]
        

                    
if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.longestPalindrome("cbbd"))