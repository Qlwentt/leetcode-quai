class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        path = [item for item in path if item != ""]
        
        stack = []
        
        for item in path:
            if item == ".":
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)
#     def getPath(pwd,cd):
#         if not cd:
#             return pwd
        
#         if cd[0] == "/":
#             pwd = ""
            
#         path = pwd + "/" + cd
#         path = path.split("/")
#         stack = []
#         for item in path:
#             if item == ".":
#                 continue
#             elif item == "..":
#                 if stack:
#                     stack.pop
#             else:
#                 if item:
#                     stack.append(item)