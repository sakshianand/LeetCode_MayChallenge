class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me=nums[0]
        count=0
        for num in nums:
            if me == num:
                count+=1
            else:
                count-=1
            if count ==0:
                me=num
                count=1
            
        return me
    
    
