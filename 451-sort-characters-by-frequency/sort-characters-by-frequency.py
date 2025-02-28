class Solution:
    def frequencySort(self, s: str) -> str:
        char_to_count = defaultdict(int)
        for char in s:
            char_to_count[char] += 1

        counts_to_char = defaultdict(list)
        for char, count in char_to_count.items():
            counts_to_char[count].append(char)
        
        answer = []
        for count in range(len(s),0,-1):
            for char in counts_to_char[count]:
                answer.append(char*count)
        
        return "".join(answer)
        
        

        