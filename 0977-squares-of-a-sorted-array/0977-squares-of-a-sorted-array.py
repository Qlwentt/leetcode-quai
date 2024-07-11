class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # [-4,-1,0,3,10]
        #   16 1 0 9 100
        answer = []
        last_negative = None
        for i, num in enumerate(nums):
            if num < 0:
                last_negative = i
            answer.append(num*num)
        
        if last_negative is None:
            return answer
        a = answer[(last_negative+1):]
        b = answer[:last_negative+1][::-1]
        def merge(a,b):
            answer = []
            p1 = 0
            p2 = 0
            while p1 < len(a) or p2 < len(b):
                val1 = a[p1] if p1 < len(a) else float('inf')
                val2 = b[p2] if p2 < len(b) else float('inf')
                
                if val1 < val2:
                    p1 += 1
                    answer.append(val1)
                else:
                    p2 += 1
                    answer.append(val2)
            return answer
        return merge(a,b)