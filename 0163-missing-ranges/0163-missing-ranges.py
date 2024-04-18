class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        answer = []
        if nums[0] != lower:
            answer.append([lower, nums[0]-1])
            
        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                answer.append([nums[i]+1, nums[i+1]-1])
        
        if nums[-1] != upper:
            answer.append([nums[-1]+1, upper])
            
        def formatt(answer):
            formatted = []
            for start, end in answer:
                if start == end:
                    formatted.append(str(start))
                else:
                    formatted.append(f"{start}-{end}")
            return formatted
        print(formatt(answer))
        return answer