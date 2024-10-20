class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for char in expression:
            if char in "!&|(":
                stack.append(char)
            elif char == "t":
                stack.append(True)
            elif char == "f":
                stack.append(False)
            elif char == ")":
                items = []
                while stack[-1] != "(":
                    items.append(stack.pop())
                stack.pop()
                command = stack.pop()
                if command == "!":
                    stack.append(not(items[0]))
                elif command == "&":
                    stack.append(all(items))
                elif command == "|":
                    stack.append(any(items))
        return stack[-1]
                
            
                
        
            
        