class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        start_len = len(str(low))
        end_len = len(str(high))
        
        for length in range(start_len, end_len+1):
            num = int("".join([str(i+1) for i in range(length)]))
            incr = int("".join(["1"] * length))
            
            while num <= high:
                if num >= low:
                    answer.append(num)
                if int(str(num)[-1]) >= 9:
                    break
                num += incr
        
        return answer
            
        
        
            
            
            