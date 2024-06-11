class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        
        while True:
            if memory1 >= memory2:
                if memory1 - i < 0:
                    return [i, memory1, memory2]
                memory1 -= i
            else:
                if memory2 - i < 0:
                    return [i, memory1, memory2]
                memory2 -= i
            
            i += 1
        return 
            
        