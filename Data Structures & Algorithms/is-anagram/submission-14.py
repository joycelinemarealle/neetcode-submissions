class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char,0) + 1
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0)+1

        #comapre
        for key in s_dict:
            if s_dict[key] != t_dict.get(key,0):
                return False
        return True


        #anagram capital,space amount of letter same t=2 , t=2
        #s,t
        #anagrams must have same length, same amouunt of each char
        #return True

        #have a quick fail if lens(s) not same at t , return False
        #if length same when can invest further the count of each char
        #keep count of each chart in dic for both s, t
        #need to loop through key of s_dic see if s_dic[key] the count matches that of value in dic_t. if not then return False
        #end function return True since passed all constraints
        #Big O time (n)--> 
        #Big O space --> (1) dictionary