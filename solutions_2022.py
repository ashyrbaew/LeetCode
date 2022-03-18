## 20. Valid Parentheses

`class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {')':'(',
                ']':'[',
                '}':'{'}

        for c in s:
            if c in pMap:
                if not stack or pMap[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
`
