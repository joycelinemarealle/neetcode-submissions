class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dic = {}
        t_dic = {}

        #firt disqualifier, no need to proceed if this does not work
        if len(s)!= len(t):
            return False

        #add counts in dictionary
        for sval in s:
            s_dic[sval] = s_dic.get(sval, 0) + 1 
        
        for tval in t:
            t_dic[tval] = t_dic.get(tval, 0) + 1
        
        #compare counts of key
        for key in s_dic:
            if s_dic[key]!= t_dic.get(key,0):
                return False
           
        return True
        #return s_dic == t_dic



        
        #same length, case letters for string to mean the same
        #check length of two string not same return false
        #loop hrough s and track counts of each letter
        #loop through t track counts of each letter
        #compare counts of each letter if not same return False
        #return true
        #Time Big O(2m) => Big O(m) worst case loop through all
        # Memory Big O(1) 