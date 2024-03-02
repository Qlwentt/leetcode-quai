class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        last = self.countAndSay(n-1)
        count = 0
        prev = None
        answer = []
        for num in last:
            if prev and num != prev:
                answer.append(str(count) + prev)
                count = 1
            else:
                count += 1
            prev = num
        answer.append(str(count) + prev)
        return "".join(answer)
        