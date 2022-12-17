class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        each_bank_numberone = []
        element = 0
        for i in accounts:
            for j in i:
                element += j
            each_bank_numberone.append(element)
            element = 0    
        return max(each_bank_numberone)