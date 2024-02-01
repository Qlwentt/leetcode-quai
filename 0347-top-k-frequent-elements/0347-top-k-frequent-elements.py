class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        # 1: 3
        # 2: 2
        # 3: 1
        freqList = [[] for _ in range(max(counter.values())+1)]
        
        for num, count in counter.items():
            freqList[count].append(num)
        
        answer = []
        for i in range(len(freqList)-1,0,-1):
            for num in freqList[i]:
                if k > 0:
                    answer.append(num)
                    k -= 1
                else:
                    break
        return answer
            
            