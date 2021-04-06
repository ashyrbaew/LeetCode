# LeetCode
LeetCode solved problems - Python3


<<<<<<< HEAD
### 1614. Maximum Nesting Depth
```python
=======
#1614. Maximum Nesting Depth
>>>>>>> fbf93dc39050c067f4579feda6f11b21a9955322
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
```
