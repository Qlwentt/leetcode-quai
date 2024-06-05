class Solution:
    def minPartitions(self, n: str) -> int:
#         3 tens
#         2 ones
        
#         82734
        
#         8 ten thousands
#         2 thousands
#         7 hundreds
#         3 tens
#         4 ones
        answer = float('-inf')
        for digit in n:
            answer = max(int(digit), answer)
            
        return answer