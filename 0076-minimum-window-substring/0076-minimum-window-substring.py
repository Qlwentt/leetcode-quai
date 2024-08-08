class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_s = defaultdict(int)
        count_t = {}
        
        for char in t:
            count_t[char] = count_t.get(char,0) + 1
        
        
        l = 0
        ans_l = None
        ans_r = None
        min_length = float('inf')
        for r in range(len(s)):
            count_s[s[r]] += 1
            while all(count_s[item_t] >= count_t[item_t] for item_t in count_t):
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    ans_l = l
                    ans_r = r
                count_s[s[l]] -= 1
                l += 1
        return s[ans_l:ans_r+1] if min_length != float('inf') else ""
                