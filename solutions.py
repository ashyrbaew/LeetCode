import pdb
class Solution:
    def isValid(self, s):
        stack = []
        par={"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in par:
                if not stack or stack.pop() != par[char]:
                    return False
            else:
                stack.append(char)

        return not stack

test = Solution()
res = test.isValid("()")
print(res)