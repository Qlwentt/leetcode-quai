class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        change1 = ""
        change2 = ""
        for digit in num:
            if int(digit) < 9:
                change1 = digit
                break
            
        max_num = num.replace(digit, "9")
        min_num = num.replace(num[0], "0").lstrip("0") or "0"
        return(int(max_num)-int(min_num))