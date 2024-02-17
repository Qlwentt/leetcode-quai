class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
  #     [[1,3],[2,1],[3,2]] [[2,3],[3,2]]
   #                   P                   
   #                                 Q
    #  [[2,3]][6,1][9,2]
    
#     [[1,3],[2,3]] [[6,3],[3,3]]
#              P             Q
        
#     [6,6]

        p1 = 0
        p2 = 0
        answer = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            num1, count1 = encoded1[p1]
            num2, count2 = encoded2[p2]
            
            ansNum = num1 * num2
            ansCount = min(count1, count2)
            if count1 < count2:
                p1 += 1
                newCount = count2 - count1
                encoded2[p2][1] = newCount
            elif count2 < count1:
                p2 += 1
                newCount = count1 - count2
                encoded1[p1][1] = newCount
            else: # equal
                p1 += 1
                p2 += 1
                
            if answer and answer[-1][0] == ansNum:
                answer[-1][1] += ansCount
            else:
                answer.append([ansNum, ansCount])
                
        return answer
            