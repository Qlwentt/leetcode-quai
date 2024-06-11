class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
#         lo = 0
#         hi = cheeseSlices
        
#         while lo <= hi:
#             mid = (lo+hi) // 2
            
#             jumbo = mid
#             small = cheeseSlices - mid
#             curTomato = jumbo * 4 + small * 2
#             if curTomato == tomatoSlices:
#                 return [jumbo, small]
#             if curTomato > tomatoSlices:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return []

# 4J + 2S = tomato
# 4J = tomato - 2S
# J = (tomato - 2S) / 4
#  J + S = cheese
# (tomato - 2S)
# ------------- + S = cheese
#      4
# tomato/4 -1/2S + S = cheese
# tomato/4 + 1/2S = cheese
# 1/2S = cheese - tomato/4
# S = 2* (cheese-tomato/4)

        S = 2 * (cheeseSlices- (tomatoSlices/4))
        J = cheeseSlices - S
        
        
        
        if 4*J + 2*S == tomatoSlices and J+S == cheeseSlices and J>=0 and S>= 0 and J%1 == 0 and S%1==0:
            return [int(J), int(S)]
        return []
        
        
        