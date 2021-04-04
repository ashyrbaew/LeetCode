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



#1021. Remove Outermost Parentheses
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
                


#1816. Truncate Sentence
class Solution:
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])




#1812. Determine Color of a Chessboard Square
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
        
        