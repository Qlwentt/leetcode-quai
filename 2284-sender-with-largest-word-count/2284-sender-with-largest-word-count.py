class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senders_count = collections.defaultdict(int)
        
        for i, message in enumerate(messages):
            sender = senders[i]
            senders_count[sender] += len(message.split(" "))
            
        sorted_senders = [key for key in sorted(senders_count, key=lambda x: (senders_count[x], x), reverse=True)]
        print(sorted_senders)
        return sorted_senders[0]
                          