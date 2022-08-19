class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations = { k: 0 for k in keysPressed}
        durations[keysPressed[0]] = releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            durForKey = durations[keysPressed[i]]
            
            durations[keysPressed[i]] = max(durForKey, duration)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphaIndices = {char: -(i+1) for i, char in enumerate(alphabet)}
        maxHeap = [(-duration, alphaIndices[char]) for char, duration in durations.items()]
        heapq.heapify(maxHeap)
        
        return alphabet[-maxHeap[0][1] -1]

            