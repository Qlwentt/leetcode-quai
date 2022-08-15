class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1, num2]:
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2])
                result[i1+i2] += product
                result[i1+i2+1] += result[i1+i2] // 10
                result[i1+i2] = result[i1+i2] % 10
                
        result = result[::-1]
        beg = 0
        while beg < len(result) and result[beg] == 0:
            beg += 1
        return "".join([str(num) for num in result[beg:]])