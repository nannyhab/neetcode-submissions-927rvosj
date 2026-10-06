class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        window = 0
        maxWindow = 0
        L = 0
        satisfied = 0

        for R in range(len(customers)):
            if grumpy[R] == 1:
                window += customers[R]
            else:
                satisfied += customers[R]
            
            if R - L + 1 > minutes:
                if grumpy[L] == 1:
                    window -= customers[L]
                L += 1
            
            maxWindow = max(window, maxWindow)
        return maxWindow + satisfied
        