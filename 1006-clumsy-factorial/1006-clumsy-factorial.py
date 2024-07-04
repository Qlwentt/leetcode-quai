class Solution:
    def clumsy(self, n: int) -> int:
        operator = "*/+-"
        i = 0
        stack = []
        stack.append(n)
        while n:            
            op = operator[i % 4]
            if op == "*":
                b = n - 1
                if b == 0:
                    break
                a = stack.pop()
                stack.append(a*b)
                n -= 1
            elif op == "/":
                b = n - 1
                if b == 0:
                    break
                a = stack.pop()
                n -= 1
                stack.append(int(a/b))
            elif op == "+":
                stack.append(n-1)
                n -= 1
            elif op == "-":
                stack.append(-(n-1))
                n -= 1
            i += 1
            
        return sum(stack)
                