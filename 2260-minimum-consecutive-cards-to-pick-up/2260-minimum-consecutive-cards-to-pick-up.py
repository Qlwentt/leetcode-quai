class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1
        cards_dict = collections.defaultdict(list)
        for i, card in enumerate(cards):
            cards_dict[card].append(i)
        answer = float('inf')
        for card, indexes in cards_dict.items():
            for i, j in zip(indexes,indexes[1:]):
                answer = min(j-i+1,answer)
        
        return answer