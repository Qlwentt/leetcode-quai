from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        answer = 0
        for word in words:
            chars_count_copy = chars_count.copy()
            can_make_word = True
            for char in word:
                if char not in chars_count_copy or chars_count_copy[char] <= 0:
                    can_make_word = False
                    break
                else:
                    chars_count_copy[char] -= 1
            if can_make_word:
                answer += len(word)
        return answer
            
                    