from sortedcontainers import SortedList
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        sorted_list = SortedList(words)
        count = 0
        extra = False
        while sorted_list:
            word = sorted_list.pop(0)
            if word[::-1] in sorted_list:
                count += 2
                sorted_list.remove(word[::-1])
            elif word[0]+word[0] == word:
                extra = True
        return (count+extra) * 2
  
    