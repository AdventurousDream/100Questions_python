class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len1, len2 = len(s), len(p)

        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        for j in range(1, len2 + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if p[j - 1] == s[i-1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i-1]:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    elif p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[len1][len2]



if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.isMatch("aab","c*a*b"))