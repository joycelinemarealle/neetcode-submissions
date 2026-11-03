class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr= ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
        
        #create an empty string
        #loop through each char in input check if alpha numeric then convert to lower and to new str
        #compare new stri with its reverse if equal return true if not return false
