class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        splitPath = path.split('/')
        for directory in splitPath:
            if directory == "" or directory == ".":
                continue
            if directory == "..":
                if result:
                    result.pop()
                continue
            directory = directory.replace('/', '')
            result.append(directory)
            
        return "/" + "/".join(result) 