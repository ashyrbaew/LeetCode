import pdb
class Solution:
    def isValid(self, s):
        stack = []
        par={"}":"{", "]":"[", ")":"("}

        for i,j in enumerate(s):
            print(i, stack)
            if j in par:
                if not stack or stack.pop() != par[j]:
                    return False
            else:
                stack.append(j)

        print("test", stack)
        return not stack

test = Solution()
res = test.isValid("()")
print(res)