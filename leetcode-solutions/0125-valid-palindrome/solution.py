class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        cleaned=""
        for char in s:
           if char.isalnum():
                cleaned = cleaned + char
        left=0
        right=len(cleaned)-1

        while left<right:
            if cleaned[left] != cleaned[right]:
                return False
            left +=1
            right-=1
        return True 
        
