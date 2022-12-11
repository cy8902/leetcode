class Solution:
    def removeElement(self,nums,val):
        idx = 0
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)
