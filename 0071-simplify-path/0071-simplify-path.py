class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for directory in path.split("/"):
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == "." or not directory:
                pass
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)