class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)] # index is count, value is list of items at that count
        
        for num, count in counter.items():
            bucket[count].append(num)
        
        answer = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                if k:
                    answer.append(num)
                    k -= 1
                else:
                    break
                    
        return answer

                
        