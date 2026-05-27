class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #default dic contains list as key #mappy charcount to list of anagrams
        
        #loop through strings
        for s in strs:
            count = [0]*26 # initialize 0 for 26 posibilities of char [0,0,0,0,0,0....]
            
            #loop through each char in string
            for c in s:
                count[ord(c)- ord("a")] +=1 #add count in the index [ 1,0,0,0,1,0,0,1]
            res[tuple(count)].append(s) #[[1,0,0,0,1,0,0,1]: eat, ] #cannot have list as key so make tuple
        
        return list(res.values()) #out list[List[str]] res.value returns view object
        
        #Time loop through each string and each char in string avg length say n,m string O(mn*26)->O(mn)
        #memory dict Big O(1)
        #input array out sublits in array
        #loop through strings array then loop through each string
        #key list with count of each letter . Value is list of anagrams matching the count
        #use scid as index to keep truck 
        #values with same count of letter