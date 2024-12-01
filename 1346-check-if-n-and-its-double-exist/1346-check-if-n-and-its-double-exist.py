class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        
        for num in arr:
            if num == 0:
                if counter[num] > 1:
                    return True
            else:
                if num * 2 in counter:
                    return True
        return False