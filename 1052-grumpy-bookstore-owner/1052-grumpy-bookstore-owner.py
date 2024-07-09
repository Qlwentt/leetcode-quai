class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #[1,0,1,2,1,1,7,5]
        #[0,1,0,1,0,1,0,1]

        total_satisfied = sum([customers * (not is_grumpy) for customers, is_grumpy in zip(customers, grumpy)])
        L = 0
        cur_grumpy = 0
        max_k_grumpy = 0
        for R in range(len(customers)):
            if R-L+1 > minutes:
                cur_grumpy -= customers[L] if grumpy[L] else 0
                L += 1
            cur_grumpy += customers[R] if grumpy[R] else 0
            
            if R-L+1 == minutes:
                max_k_grumpy = max(max_k_grumpy, cur_grumpy)
        
        
        
        
        return total_satisfied + max_k_grumpy
        