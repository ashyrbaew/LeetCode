# LeetCode
LeetCode solved problems - Python3



### 1614. Maximum Nesting Depth
```python
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
/
/
/
### 1021. Remove Outermost Parentheses
```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        p=0
        r=""
        for n in S:
            if n=="(" and p==0:
                p+=1
                continue
            elif n=="(" and p>0:
                p+=1
                r+=n
            elif n==")" and p>1:
                p-=1
                r+=n
            else:
                p=0
                continue
                
        return r
```


### 1816. Truncate Sentence
```python
class Solution:
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])




### 1812. Determine Color of a Chessboard Square
```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        if coordinates[0] =="a" or coordinates[0] =="c" or coordinates[0] =="e" or coordinates[0] =="g":
            if int(coordinates[1])%2==0:
                return True
            else:
                return False
        
        if coordinates[0] =="b" or coordinates[0] =="d" or coordinates[0] =="f" or coordinates[0] =="h":
            if int(coordinates[1])%2==0:
                return False
            else:
                return True
```



### 1450. Number of Students Doing Homework at a Given Time
```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int: 
        res=0
        for i in range(len(startTime)):
            if queryTime>=startTime[i] and queryTime<=endTime[i]:
                res+=1
        return res
```
                


### 832. Flipping an Image
```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        temp=0
        for n in A:
            for l in range(len(n)//2):
                if n[l]!=n[-l-1]:
                    temp = n[l]
                    n[l] = n[-l-1]
                    n[-l-1] = temp
      
            for k in range(len(n)):
                if n[k]==0:
                    n[k]=1
                else:
                    n[k]=0
        return A

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        temp=0
        for n in A:
            n.reverse()
            for k in range(len(n)):
                if n[k]==0:
                    n[k]=1
                else:
                    n[k]=0
        return A
```




### 657. Robot Return to Origin
```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for m in moves:
            if m=="U":
                y+=1
            elif m=="D":
                y-=1
            elif m=="R":
                x+=1
            else:
                x-=1
        
        if x==0 and y==0:
            return True
        else:
            return False
```



### 1742. Maximum Number of Balls in a Box
```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res=[0]*100
        if lowLimit >0 and highLimit < 10:
            return 1
        
        for n in range(lowLimit, highLimit+1):
            res[sum(int(digits) for digits in str(n))] +=1
        
        return max(res)
```




### 1460. Make Two Arrays Equal by Reversing Sub-arrays
```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```




### 1337. The K Weakest Rows in a Matrix
```python
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        r=[]
        for n in mat:
            res.append(sum(n))
        print(res)
        for l in range(k):
            r.append(res.index(min(res)))
            res[res.index(min(res))]=999999
        
        return r
```



### 1403. Minimum Subsequence in Non-Increasing Order
```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort(reverse=True)
        for n in nums:
            res.append(n)
            if sum(res) > sum(nums) - sum(res):
                return res
```