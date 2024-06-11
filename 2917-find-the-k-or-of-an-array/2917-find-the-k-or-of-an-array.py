class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        binary_nums = []
        max_len = 0
        for num in nums:
            x = bin(num)[2:]
        
            max_len = max(max_len, len(x))
            binary_nums.append(x)
        binary_nums = [("0" * (max_len-len(num))) + num for num in binary_nums]

        answer = []
        for i in range(max_len):
            times = 0
            for num in binary_nums:
                if num[i] == "1":
                    times += 1
                if times == k:
                    break
            answer.append("1" if times == k else "0")
        return int("".join(answer), 2)
        