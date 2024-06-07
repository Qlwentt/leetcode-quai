class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counts = collections.defaultdict(int)
        
        for char in licensePlate:
            if char.isalpha():
                counts[char.lower()] += 1
        shortest = float('inf')
        answer = None
        for word in words:
            counts_copy = counts.copy()
            for char in word:
                counts_copy[char] -= 1
            if all([val <= 0 for char, val in counts_copy.items()]):
                if len(word) < shortest:
                    shortest = len(word)
                    answer = word
            
        return answer
            