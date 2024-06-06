class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1
        
        cards_dict = {}
        answer = float('inf')
        for i, card in enumerate(cards):
            if card in cards_dict:
                answer = min(i - cards_dict[card] + 1, answer)
            cards_dict[card] = i
        
        return answer