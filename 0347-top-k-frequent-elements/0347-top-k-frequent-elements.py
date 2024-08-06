class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        
        for num, count in counts.items():
            bucket[count].append(num)
        answer = []
        for i in range(len(bucket)-1, 0, -1):
            for item in bucket[i]:
                if k:
                    answer.append(item)
                    k -= 1
                else:
                    break
        return answer
                 