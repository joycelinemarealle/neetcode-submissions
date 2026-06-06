class Solution:
    def isPalindrome(self, s: str) -> bool:
     #soln 2
     l, r = 0, len(s)-1
     
     while l < r:
        while l < r and not self.isalphaNumeric(s[l]):
            l += 1
        while r > l and not self.isalphaNumeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l + 1, r - 1 #move to next position
     return True

    def isalphaNumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))


    #    #soln1
    #     newStr = ""
    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower() #just all lower case non aplhanumeric
    #     return newStr == newStr[::-1] #cmpare to reversed string
    #time big O(n)
    #memory const big O(1) no storing of string just pointer

        
        
       #sol 2
       #Use two pointers from both ends. 
    #    Skip non-alphanumeric characters. 
    #    Compare lowercase characters. 
    #    If they ever differ, return False. 
    #    If the pointers cross, return True.”
       # two pointer l, r
       #loop through stirng
       #while l<r 
          #s[l] check if not alphanumeric, if not move l pointer
          #s[r] check if not isalnum if not move r pointer left
          # if alpha numeric compare lower casesnot same as lower move pointer
       #return true if looping done
       
        #sol 1
        #loop through string
        #check if alphanumeric and add to new string lowercase
        #return true if new str same as reverse
        #time Big O(n)
        #memory Big O(n) the string length number of elements