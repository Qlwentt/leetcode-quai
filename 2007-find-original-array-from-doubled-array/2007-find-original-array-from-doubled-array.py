from sortedcontainers import SortedList
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sorted_list = SortedList(changed)
        
        answer = []
        while sorted_list:
            num = sorted_list.pop(0)
            if num * 2 in sorted_list:
                sorted_list.remove(num*2)
                answer.append(num)
        return answer if len(answer) == len(changed) / 2 else []
            