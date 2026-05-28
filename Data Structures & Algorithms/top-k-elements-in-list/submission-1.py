class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} #maps num to num count
        for num in nums:
            count[num] = count.get(num,0) + 1 #adds count of each num
        #stor in arra
        arr = []
        for num,cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()
        
        #pop off and add to res
        res = []
        while len(res) < k :
            res.append(arr.pop()[1]) #pop off from array the second value which is num'
        return res

        #loop through
        #keep track of k:v num"count
        #stor in array the [count, num] pop off upto length of k' 
        #can sort the array nary from small to big
        #return array
        #time Big ) nlogn + Big O(n)
        #memory array and dic Big O(m) constant
        