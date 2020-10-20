import typing

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 0:
            return len(s)
        st = 0
        ed = 1
        res = 1
        mylist = []
        mylist.append(s[0])
        while ed < len(s):
            if s[ed] not in mylist:
                pass
            else:
                i = mylist.index(s[ed])
                del mylist[0:i + 1]
                curLen = ed - st
                res = curLen if curLen > res else res
                st = st + i + 1
            mylist.append(s[ed])
            ed = ed + 1
        
        curLen = ed - st
        res = curLen if curLen > res else res

        return res
    

if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.lengthOfLongestSubstring("abcabcbb"))