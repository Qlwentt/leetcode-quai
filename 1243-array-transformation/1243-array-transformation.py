class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = False
        while True:
            new_arr = arr.copy()
            for i in range(1, len(arr)-1):
                if arr[i] < arr[i+1] and arr[i] < arr[i-1]:
                    changed = True
                    new_arr[i] += 1
                elif arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                    changed = True
                    new_arr[i] -= 1
            arr = new_arr
            if changed == False:
                break
            changed = False
        return arr