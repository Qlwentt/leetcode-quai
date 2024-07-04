class Solution:
    def clumsy(self, n: int) -> int:
        operator = "*/+-"
        i = 0
        stack = []
        stack.append(n)
        while n-1:            
            op = operator[i % 4]
            if op == "*":
                b = n - 1
                a = stack.pop()
                stack.append(a*b)
                n -= 1
            elif op == "/":
                b = n - 1
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
                