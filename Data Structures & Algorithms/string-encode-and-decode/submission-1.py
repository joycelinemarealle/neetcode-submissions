class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        res = defaultdict(list)

        for s in strs:
            count = [0]*26 #count of char in a string #[0,0,0,.....] a-z
            for c in s:
                count[ord(c) - ord("a")] += 1 #add the count in index of each char you find [1,0,1,0,.....1] for act
            res[tuple(count)].append(s) #a listcannot be key so change to tuple
        return list(res.values())

            
       



        #hashmpa key:value, charcount": list of words
        #loop through strings for each string keep count of char
        # add to dic, put value as list of words
        #return list
        #Time Big O(nm*26) => looping through n stirngs + n avg of stirng length *26 max length
        #memory Big O(1) dictionary