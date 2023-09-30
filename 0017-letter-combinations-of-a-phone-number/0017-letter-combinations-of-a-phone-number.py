class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = { '2': 'abc', '3': 'def', '4': "ghi", '5': "jkl",
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        combs = []

        def backtrack(i, curComb):
            if len(curComb) == len(digits):
                combs.append("".join(curComb))
                return
            
            for letter in phone[digits[i]]:
                curComb.append(letter)
                backtrack(i+1, curComb)
                curComb.pop()
        if digits:
            backtrack(0, [])
        return combs
                