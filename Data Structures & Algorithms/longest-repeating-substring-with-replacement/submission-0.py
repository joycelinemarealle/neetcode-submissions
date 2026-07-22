class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #pointers, map
        count = {} #count of char in str
        res = 0 #track max len of str with same values(after replacement
        l = 0 #left pointer starts at first char

        #loop right pointer
        for r in range(len(s)):
            #check count of right value
            count[s[r]]  = 1 + count.get(s[r], 0) #intialize with zero if count empty

            #check condition to shrink window
            while (r - l + 1) - max(count.values()) > k:
                #reduce count of left value then move l pointer ->
                count[s[l]] -=1
                l+=1
            #track max len
            res = max(res,r - l + 1)
        return res

        #sliding window
        #variabe hashmap to store char, res
        #loop rig in range
        #increase count of right value
        #while condition to shrink check count of char to be replaced > than k then shrink  decrases countpf s[l]-=1,windo move l to right +
        #replacements windolen- max count of chars
        #res max(res, length of window)
        