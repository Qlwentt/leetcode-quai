class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        bucket = [0] * (len(arr) + 1) # index = frequency, value = num of numbers with that frequency
        for num, count in counts.items():
            bucket[count] += 1
        
        # [0,1,1,1,1,0,0,0,0,0, 0]
        #  0 1 2 3 4 5 6 7 8 9 10
            
        target = len(arr) // 2
        answer = 0
        for freq in range(len(bucket)-1, 0, -1):
            num_of_nums = bucket[freq]
            while target > 0 and num_of_nums > 0:
                target -= freq
                num_of_nums -= 1
                answer += 1
        return answer
        