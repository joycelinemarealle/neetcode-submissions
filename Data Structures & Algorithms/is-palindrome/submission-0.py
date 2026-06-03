class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower() #just all lower case non aplhanumeric
        return newStr == newStr[::-1] #cmpare to reversed string

        #loop through string
        #check if alphanumeric and add to new string lowercase
        #return true if new str same as reverse
        #time Big O(n)
        #memory Big O(n) the string length number of elements