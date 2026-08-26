class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         counts1 = {} #s
         counts2 = {} #t
         l = len(s)
         if len(s) != len(t):
            return False
         for i in range(l):
            if s[i] in counts1:
                counts1[s[i]] += 1;
            else:
                counts1[s[i]] = 1
         for j in range(l):
            if t[j] in counts2:
                counts2[t[j]] += 1
            else:
                counts2[t[j]] = 1
         if counts1 == counts2:
            return True
         else:
            return False
        
                