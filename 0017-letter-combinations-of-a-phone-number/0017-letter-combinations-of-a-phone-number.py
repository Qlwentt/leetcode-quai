class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i,curComb):
            if i == len(digits):
                answer.append("".join(curComb))
                return
            digit = digits[i]
            
            for char in phone[digit]:
                curComb.append(char)
                backtrack(i+1, curComb)
                curComb.pop()
                
        backtrack(0,[])
        return answer if digits else []
            