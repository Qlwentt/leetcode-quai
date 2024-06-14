class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cache_by_cells = {}
        cache_by_i = {}
        i = 0
        N = n
        
        while N:
            if tuple(cells) in cache_by_cells:
                cycle_length = len(cache_by_i)
                return cache_by_i[((n % cycle_length) -1 )%cycle_length]
            if i:
                cache_by_cells[tuple(cells)] = i-1
                cache_by_i[i-1] = cells
            new = [0] * len(cells)
            for j in range(1,len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    new[j] = 1
            
            i += 1
            cells = new
            N -= 1
            
            
            
            
        return cells
                
        
        