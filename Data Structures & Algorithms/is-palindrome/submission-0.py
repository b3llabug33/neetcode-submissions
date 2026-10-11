class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        b = len(s) - 1
        f = 0
        st = ""

        for a in range(l):
            if char.isalnum():
                st += s[a];
            else:
                return False
        
        st = st.replace(" ", "")


        if l % 2 == 0:
            for i in range(l // 2):
                if s[f] == s[b]:
                    f += 1
                    b -= 1
                else:
                    return False
            return True
        else:
            for j in range((l // 2) - 1):
                if s[f] == s[b]:
                    f += 1
                    b -= 1
                else:
                    return False
            return True


        