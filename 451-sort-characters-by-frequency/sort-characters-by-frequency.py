class Solution:
    def frequencySort(self, s: str) -> str:
        # dictionary and bucket sort
        # char_to_count = defaultdict(int)
        # for char in s:
        #     char_to_count[char] += 1

        # counts_to_char = defaultdict(list)
        # for char, count in char_to_count.items():
        #     counts_to_char[count].append(char)
        
        # answer = []
        # for count in range(len(s),0,-1):
        #     for char in counts_to_char[count]:
        #         answer.append(char*count)
        
        # return "".join(answer)
    # Time: O(N)
    # Space: O(N)  

    # using Counter

        counts = collections.Counter(s)
        answer = []
        for char, count in counts.most_common():
            answer.append(char*count)
        return "".join(answer)
    # Time: O(NlogN)
    # Space: O(N)



        

        