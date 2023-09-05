class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10        
        return x == reversedNum or x == reversedNum // 10
        
#         if x < 0:
#             return False
        
#         n = 0
#         num = x
#         while num != 0:
#             num = num // 10
#             n += 1
#         reversedNum = 0

#         for i in range(n//2, 0, -1):
#             digit = x  % 10
#             reversedNum += digit * 10 ** (i-1)
#             x = x // 10
#         return x == reversedNum if n % 2 == 0 else x // 10 == reversedNum
        
#         x = str(x)
#         L = 0
#         R = len(x) -1
        
#         while L < R:
#             if x[L] != x[R]:
#                 return False
#             L += 1
#             R -= 1
#         return True

# 1221 
#   12
# 12

# 12221
# 1221

# 1221 // 10 = 122 r (1 * 10^0) 1
# 122 // 10  = 12 r (2 * 10^1)  20      