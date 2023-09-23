from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)] # frequency, items
        
        for num, count in count.items():
            freq[count].append(num)
        
        answer = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                answer.append(num)
                k -= 1
                if k == 0:
                    return answer
        
        
        