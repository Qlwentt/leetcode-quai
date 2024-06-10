class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_num = hex(int(num))
        hex_num = hex_num[2:]
        answer = list(hex_num)
        
        for i in range(len(hex_num)):
            if hex_num[i] == "1":
                answer[i] = "I"
            elif hex_num[i] == "0":
                answer[i] = "O"
            elif hex_num[i].isalpha():
                answer[i] = hex_num[i].upper()
            else:
                return "ERROR"
        return "".join(answer)
        