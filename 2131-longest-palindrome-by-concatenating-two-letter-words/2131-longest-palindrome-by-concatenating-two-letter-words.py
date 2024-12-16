from sortedcontainers import SortedList
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # sorted_list = SortedList(words)
        # count = 0
        # extra = False
        # while sorted_list:
        #     word = sorted_list.pop(0)
        #     if word[::-1] in sorted_list:
        #         count += 2
        #         sorted_list.remove(word[::-1])
        #     elif word[0]+word[0] == word:
        #         extra = True
        # return (count+extra) * 2
        
        count_words = collections.Counter(words)
        pali_words = 0
        extra = False
        
        while count_words:
            word, count = count_words.popitem()
            if count != 1:
                count_words[word] = (count - 1)
            if word[::-1] in count_words:
                pali_words += 2
                count_words[word[::-1]] -= 1
                if count_words[word[::-1]] == 0:
                    del count_words[word[::-1]]
            elif word[0]+word[0] == word:
                extra = True
        return (pali_words + extra) *2
  
    