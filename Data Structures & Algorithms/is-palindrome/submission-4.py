class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pointers
        l , r = 0, len(s)-1
        
        #loop
        while l < r :
            while l<r and not self.isalphaNumeric(s[l]):
                l +=1
            while l<r and  not self.isalphaNumeric(s[r]):
                r -=1
            if  s[l].lower() != s[r].lower():
                return False
    
            l,r = l +1 , r-1 #move to next poistion
        return True
            

    def isalphaNumeric(self, c):
        #A-Z,a-z, 0-9
        #returns true
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


        #constraints only lower case, remove non alpha,
        #use two ponter l , r, chekc if alpha numeric if not move pointers, if yes check if same if not return false
        #isalphaNumeric ( i can use asci using ord())
        #loop through s, check if not alpha numeric skip ( l -> )
        # if at right not alpha num r <-
        # if it is check lowercase if the same andreturn true then move pointer r <-
        #time Big O(n) n number char looping
        #memory Big O(1) constant space, pointer