class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        strNum = list(str(num))
        if num < 0:
            strNum = strNum[1:]
            strNum.sort(reverse=True)
        else:
            strNum.sort()
        i = 0
        while i + 1 < len(strNum) and strNum[0] == "0":
            strNum[0], strNum[i+1] = strNum[i+1], strNum[0]
            i += 1
            
            
        answer = int("".join(strNum))
        return answer if num > 0 else -answer