class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        answer = []
        count = 0
        prevNum = None
        for num in prev:
            if prevNum != None and num != prevNum:
                answer.append(str(count)+prevNum)
                count = 1
            else:
                count += 1
            prevNum = num
        answer.append(str(count)+prevNum)
        return "".join(answer)
                
                
        
        