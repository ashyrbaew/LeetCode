#1614. Maximum Nesting Depth
class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        m=[0]
        for a in s:
            if a=="(":
                d+=1
                m.append(d)
            elif a==")":
                d-=1
        
        return max(m)


