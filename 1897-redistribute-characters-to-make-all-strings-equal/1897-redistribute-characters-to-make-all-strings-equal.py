class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total = collections.defaultdict(int)
        
        for word in words:
            for char in word:
                total[char] += 1
        
        number = len(words)
        
        for char, count in total.items():
            if (count / number) % 1 != 0:
                return False
        return True
                
        