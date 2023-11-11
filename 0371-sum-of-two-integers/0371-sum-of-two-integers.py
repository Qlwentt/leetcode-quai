class Solution:
    def getSum(self, a: int, b: int) -> int:
         # 1
       # 10100
       # 11110
    # --------
       # 100010
       # 110010
        
            
        def add(a,b):
            carry = 0
            binary = []
            while a or b or carry:
                digitA = a & 1
                digitB = b & 1

                digit = digitA ^ digitB ^ carry
                carry = (digitA & digitB) or (digitA & carry) or (digitB & carry) 
                binary.append(str(digit))

                a = a >> 1
                b = b >> 1

            binary.reverse()
            return int("".join(binary), 2) 
        
        def subtract(a,b):
            A, B = a, b
            if A == B:
                return 0
            if b > a:
                a,b = b,a
           
            # 14-16
            # 16-14
             # 10000
             # 01100
             # 
             # -----
            #      00
            borrow = 0
            binary = []
            while a or b:
                digitA = a & 1
                digitB = b & 1

                if digitA and borrow:
                    digitA = not digitA
                    borrow = 0
                digit = digitA ^ digitB ^ borrow
                borrow = (digitB and not digitA) or (borrow and not digitA)
                binary.append(str(digit))

                a = a >> 1
                b = b >> 1
            binary.reverse()
            num = int("".join(binary), 2) 
            
            if A > B:
                return num
            else:
                return -num
            
        
        if ((a < 0 and b >= 0) or (b<0 and a>= 0)):
            if a < 0:
                return subtract(abs(b), abs(a))
            else:
                return subtract(abs(a), abs(b))
        elif a < 0 and b < 0:
            return -add(abs(a), abs(b))
        else:
            return add(a,b)
        # xOR to get digit
        # & to get carry
        
        
        
        
        