class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pointers
        l , r = 0, len(s)-1
        
        #loop
        while l < r :
            if not self.isalphaNumeric(s[l]):
                l +=1
            elif not self.isalphaNumeric(s[r]):
                r -=1
            elif s[l].lower() == s[r].lower():
                r-=1
                l+=1
            else:
                return False
        return True
            



    def isalphaNumeric(self, c):
        #A-Z,a-z, 0-9
        #returns true
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


        #constraints only lower case, remove non alpha,
        #use two ponter l , r
        #isalphaNumeric ( i can use asci using ord())
        #loop through s, check if not alpha numeric skip ( l -> )
        # if at right not alpha num r <-
        # if it is check lowercase if the same andreturn true then move pointer r <-
        #time Big O(n) n number char looping
        #memory Big O(1) constant space, pointer