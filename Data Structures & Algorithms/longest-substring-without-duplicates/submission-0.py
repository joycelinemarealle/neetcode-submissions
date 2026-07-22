class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        charSet = set()        
        res = 0 #store max length

#right pointer loops in range of s
        for r in range(len(s)):
            #if duplicate remove from set and move pointer
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            #add right char in set
            charSet.add(s[r])
            #update max
            res = max(res, r - l + 1)
        return res

        #Sliding window, l, r pointer Big O(n)
        #l =0, r loop in range of s
        #to shrink the window, there is duplicate. So, I will use a set to store the char as i go through the s
        #if duplicate shrink window move l +=1 and remove the left char from set
        #add left value in set, check max length (r-l+1)
        #BigO(n) max looping through string, time big o(1) variables