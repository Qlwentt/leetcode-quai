class Solution:
    def entityParser(self, text: str) -> str:
        parse = {"&quot;": "\"", "&apos;": "\'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        
        stack = [[]]
        for char in text:
            if char == "&":
                stack.append([char])
            elif char == ";":
                stack[-1].append(char)
                stack.append([])  
            else:
                stack[-1].append(char)
        
        for i, item in enumerate(stack):
            if item and item[0] == "&" and item[-1] == ";":
                entity = "".join(item)
                if entity in parse:
                    stack[i] = [parse[entity]]
        
        return "".join([item for sublist in stack for item in sublist])
                
        