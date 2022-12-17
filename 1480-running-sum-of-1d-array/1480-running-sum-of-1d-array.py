class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        pls = 0
        for i in nums:
            pls += i
            answer.append(pls)
        return answer