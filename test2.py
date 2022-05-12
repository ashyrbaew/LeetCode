s="alksjdghalkjghakjsdfa;lskdjfa;kshjga"
def longestPalindrome(s):
    t = f"$#{'#'.join(list(s))}#*"
    n = len(t)
    p = [0] * n
    c = r = cm = rm = 0
    for i in range(1, n-1):
        p[i] = min(p[2*c-i], r-i) if i < r else 1
        while t[i-p[i]] == t[i+p[i]]: 
            p[i] += 1 
        if p[i] > rm: 
            cm, rm = i, p[i]
        if i+p[i] > r: 
            c, r = i, i+p[i]
    print(s[(cm-rm)//2:(cm+rm-1)//2])
    return s[(cm-rm)//2:(cm+rm-1)//2]
