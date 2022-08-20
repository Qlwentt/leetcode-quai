class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        for log in logs:
            split = log.split(" ")
            if split[1].isdigit():
                digitLogs.append(log)
            else:
                n = len(split[0])
                letterLogs.append((log[n+1:], log[:n+1]))
                        
        
        letterLogs.sort()
        letterLogs = [ident+log for log, ident in letterLogs]
        
        answer = []
        for log in letterLogs:
            answer.append(log)
        for log in digitLogs:
            answer.append(log)
            
        return answer
        