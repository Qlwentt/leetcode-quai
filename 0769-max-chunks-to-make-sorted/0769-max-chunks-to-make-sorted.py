class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        def max_chunks(sub_array, new_array):
            if len(sub_array) == 0:
                return 0 if new_array == sorted(arr) else float('-inf')
            
            
            cur_max = float('-inf')
            for i in range(len(sub_array)):
                chunk = sorted(sub_array[:i+1])
                result = max_chunks(sub_array[i+1:], new_array + chunk)
                if result != float('-inf'):
                    result += 1
                cur_max = max(result, cur_max)
                
            return cur_max
        
        return max_chunks(arr,[])
                
            
            
                
        