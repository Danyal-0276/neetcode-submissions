class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        SC = {}
        TC = {}

        for i in range(len(s)):
            temp = s[i]
            temp1 = t[i]
            SC[temp] = 1 + SC.get(temp, 0)
            TC[temp1] = 1 + TC.get(temp1, 0)

        return SC == TC
