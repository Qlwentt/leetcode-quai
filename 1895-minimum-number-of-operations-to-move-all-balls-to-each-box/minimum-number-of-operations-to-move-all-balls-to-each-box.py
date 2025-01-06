class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        "0 0 1 0 1 1"
        [0,0,0,1,2,0]
        for i, box in enumerate(boxes):
            if box == "1":
                for j in range(i):
                    answer[j] += i - j
                for j in range(min(i+1, len(boxes)), len(boxes)):
                    answer[j] += j - i
        
        return answer