class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # [1,3],[2,2],[3,7]
        # -----
        #   -
        #     ---------
        # 1 2 3 4 5 6 7
        count = 0
        for start, end in zip(startTime, endTime):
            if queryTime >= start and queryTime <= end:
                count += 1
        
        return count