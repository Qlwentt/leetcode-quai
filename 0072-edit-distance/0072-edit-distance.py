class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i1, i2):
            if i1 >= len(word1) and i2 >= len(word2):
                return 0
            
            if i1 >= len(word1) and i2 < len(word2):
                return len(word2[i2:])
            
            if i2 >= len(word2) and i1 < len(word1):
                return len(word1[i1:])
            
            if (i1, i2) in memo:
                return memo[(i1,i2)]
        
            if word1[i1] != word2[i2]:
                #insert 
                insert = 1 + dfs(i1, i2+1)

                # delete
                delete = 1 + dfs(i1+1, i2)

                # replace
                replace = 1 + dfs(i1+1, i2+1)
                   
                memo[(i1,i2)] = min(insert, delete, replace)
            else:
                memo[(i1,i2)] = dfs(i1+1, i2+1)
            return memo[(i1,i2)]
            
        
        return dfs(0, 0)
                    