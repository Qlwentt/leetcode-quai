class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        l = 0
        largest = float("-inf")
        for r in range(len(num)):
            if num[r] != num[l] or r-l+1 >3:
                l = r
            if r - l + 1 == 3:
                largest = max(int(num[r]), largest)
        return str(largest) * 3 if largest != float('-inf') else ""
        