class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotate = {"0":"0", "1":"1", "8":"8", "2":"5", "5":"2", "6":"9", "9":"6"}
        count = 0
        for i in range(1,n+1):
            rotated = []
            num = str(i)
            for digit in num:
                if digit in rotate:
                    rotated.append(rotate[digit])
                else:
                    rotated = []
                    break
            count += len(rotated) > 0  and num != "".join(rotated)
        return count