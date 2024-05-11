class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            s = s.split(".")
            s = [item for item in s if item != ""]
            if len(s) != 4:

                return "Neither"
            for part in s:
                if part[0] == "0" and len(part)>1:
                    return "Neither"
                if not part.isdigit():
                    return "Neither"
                num = int(part)
                if num < 0 or num > 255:
                    return "Neither"
            return "IPv4"
        def isIPv6(s):
            s = s.split(":")
            s = [item for item in s if item != ""]
            validChars = set(list('abcdefABCDEF0123456789'))
            if len(s) != 8:
                return "Neither"
            for item in s:
                if len(item) < 1 or len(item) > 4:
                    return "Neither"
                for char in item:
                    if char not in validChars:
                        return "Neither"
            return "IPv6"
        if queryIP.count(".") == 3:
            return isIPv4(queryIP)
        if queryIP.count(":") == 7:
            return isIPv6(queryIP)
        return "Neither"
        
        
            
            
                
                
        