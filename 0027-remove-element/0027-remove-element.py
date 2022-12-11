class Solution:
    def removeElement(self,nums,val):
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)
