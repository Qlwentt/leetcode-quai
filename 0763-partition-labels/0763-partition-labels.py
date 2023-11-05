class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {}

        for i, char in enumerate(s):
            lastOcc[char] = i
            
        end = 0
        size = 0
        answer = []
        for i, char in enumerate(s):
            last = lastOcc[char]
            end = max(end, last)
            size += 1
            
            if i == end:
                answer.append(size)
                size = 0
        return answer