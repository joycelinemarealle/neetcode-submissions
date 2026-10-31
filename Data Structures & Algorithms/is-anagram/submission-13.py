class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dic = {}
        t_dic = {}

        if len(s) != len(t):
            return False
        for s_char in s:
            #add count .get
           s_dic[s_char] = s_dic.get(s_char,0) + 1
        
        for t_char in t:
            t_dic[t_char] = t_dic.get(t_char,0)+ 1
        
        #then compare the count of each char in s vs t
        for key in s_dic:
            if s_dic[key] != t_dic.get(key,0):
                return False
        return True


          #easy fails check if two words not same length -> False
        #if length same, then check content
        #loop through string store count of every char
        #check count for every char in s, t and store in dic
        #then check for every char if in t and have same count. if not return False
        #if complete then True