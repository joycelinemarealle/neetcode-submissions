class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {} #map num to count

        for num in nums:
            count[num] = count.get(num, 0) + 1 #add the counts
        
        #sort dictionnary
        arr = []
        for num , cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        
        res = []

        while len(res)< k:
            res.append(arr.pop()[1])
        return res
        

        #hashmpa array count[count] values list
        #original thougths
        #hashmap k:v num:count
        #loop through nums to add count
        #need to check the top k in dic return the key in [] --> add to list
        # then need to sort based on first numbner [cnt, num] from ascedning min to max
        #pop until result arr less than k
        #Time loop Big O nlogn for sorting
        #memory Big(n) store in hashmap+array
