class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1 = 0
        p2 = 0
        p3 = 0
        answer = []
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            num1 = arr1[p1]
            num2 = arr2[p2]
            num3 = arr3[p3]
            
            if num1 == num2 == num3:
                answer.append(num1)
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                max_num = max(num1,num2,num3)
                if max_num == num1:
                    p2 += 1 if num2 != num1 else 0
                    p3 += 1 if num3 != num1 else 0
                elif max_num == num2:
                    p1 += 1 if num1 != num2 else 0
                    p3 += 1 if num3 != num2 else 0 
                else: # max_num == num3:
                    p1 += 1 if num1 != num3 else 0
                    p2 += 1 if num2 != num3 else 0
        return answer
                    
        