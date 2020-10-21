class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        size = 0
        for ch in s:
            if size == 0:
                if ch in [')',']','}']:
                    return False
                mystack.append(ch)
                size += 1
            else:
                if ch in ['(','[','{']:
                    mystack.append(ch)
                    size += 1
                else:
                    if ch == ')' and mystack[-1] == '(':
                        mystack.pop()
                        size -= 1
                    elif ch == ']' and mystack[-1] == '[':
                        mystack.pop()
                        size -= 1
                    elif ch == '}' and mystack[-1] == '{':
                        mystack.pop()
                        size -= 1
                    else:
                        return False
        return size == 0



if __name__ == '__main__':
    solveObj = Solution()
    print(solveObj.isValid("([)]"))