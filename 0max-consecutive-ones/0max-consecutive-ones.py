class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        local_max = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                # print(local_max, tmp)
                local_max = max(local_max, tmp)
                tmp = 0
        else:
            local_max = max(local_max, tmp)
        return local_max