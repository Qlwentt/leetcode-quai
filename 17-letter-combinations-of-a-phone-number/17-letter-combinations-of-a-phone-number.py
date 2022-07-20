class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
     
        result = []
        
        def backtrack(i, combo):
            if len(digits) == 0:
                return result
            if len(combo) == len(digits):
                result.append("".join(combo))
                return
            currentDigit = digits[i]
            
            for letter in numMap[currentDigit]:
                combo.append(letter)
                backtrack(i+1, combo)
                combo.pop()
        backtrack(0,[])
        return result
                