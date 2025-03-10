class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        answer = []
        
        def backtrack(i, curComb):
            if i == len(digits):
                answer.append("".join(curComb))
                return
            
            for char in phone[digits[i]]:
                curComb.append(char)
                backtrack(i+1,curComb)
                curComb.pop()
                
        if digits:
            backtrack(0,[])
            
        return answer
    
# Time: O(4^N * N)
# Space: O(N)