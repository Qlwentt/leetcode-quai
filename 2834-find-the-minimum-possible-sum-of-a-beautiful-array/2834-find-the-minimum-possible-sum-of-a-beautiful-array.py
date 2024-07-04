class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # i = 1
        # seen = 0    
        # answer = 0
        # while n: 
        #     if target - i in seen:
        #         i+=1
        #     else:
        #         answer += i
        #         seen.add(i)
        #         i += 1
        #         n -= 1
        # return answer % (10**9+7)
        
        # variable to hold sum
        answer = 0

        # take half of target
        half = target//2

        if (half >= n):
            # if half of the target is greater than number of elements in beautiful array
            # Beautiful array will simply contain first n positive numbers
            answer = (n*(2 + n - 1))//2
        else:
            # Beautiful array will contain first target//2 positive numbers
            answer = (half*(2 + half -1)//2)

            # Beautiful array will contain n - half positive elements starting from target
            rem = n - half
            answer += (rem * (2*target + rem-1)) // 2
        
        return answer % (10**9+7)
                
            
        