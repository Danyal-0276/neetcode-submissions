class Solution:
    def isPalindrome(self, s: str) -> bool:

        new=''
        for x in s:
            if x.isalnum():
                new+=x.lower()
        return new==new[::-1]        
        