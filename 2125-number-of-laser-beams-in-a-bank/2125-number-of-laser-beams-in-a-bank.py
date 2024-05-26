class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devicesCount = collections.defaultdict(int)
        for r, row in enumerate(bank):
            for char in row:
                if char == "1":
                    devicesCount[r] += 1
                
        answer = 0
        r1s = list(devicesCount.keys())
        for i in range(len(r1s)):
            r1 = r1s[i]
            for j in range(i+1,len(r1s)):
                r2 = r1s[j]
                noDevices = True
                for k in range(r1+1, r2):
                    if devicesCount[k] > 0:
                        noDevices = False
                if noDevices:
                    answer += (devicesCount[r1] * devicesCount[r2])
        return answer
                    
                    
                