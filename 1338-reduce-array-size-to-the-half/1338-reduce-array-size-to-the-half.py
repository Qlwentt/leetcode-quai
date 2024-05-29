class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        bucket = [0] * (len(arr) + 1) # index = frequency, value = num of numbers with that frequency
        for num, count in counts.items():
            bucket[count] += 1
            
        target = len(arr) // 2
        answer = 0
        for freq in range(len(bucket)-1, 0, -1):
            num_of_nums = bucket[freq]
            if num_of_nums:
                max_to_subtract = math.ceil(target / freq)
                num_to_subtract = min(max_to_subtract, num_of_nums)
                target -= freq * num_to_subtract
                answer += num_to_subtract
                if target <= 0:
                    break
        return answer
        