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
     
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(numMap[digits[0]])
        
        digitList = list(digits)
        currentDigit = digitList.pop()
        prevCombos = self.letterCombinations("".join(digitList))
        answer = []
        for combo in prevCombos:
            comboList = list(combo)
            addLetters = numMap[currentDigit]
            for addLetter in addLetters:
                answer.append("".join(comboList[:]+[addLetter]))
        return answer