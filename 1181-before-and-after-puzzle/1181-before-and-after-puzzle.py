from sortedcontainers import SortedSet
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        answer = SortedSet()
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i == j:
                    continue
                phrase1 = phrases[i].split(' ')
                phrase2 = phrases[j].split(' ')
                
                if phrase1[-1] == phrase2[0]:
                    # phrase1 ends with the same word that phrase2 starts
                    puzzle = phrase1 + phrase2[1:]
                
                elif phrase2[-1] == phrase1[0]:
                    # phrase2 ends with the same word that phrase1 starts
                    puzzle = phrase2 + phrase1[1:]
                else:
                    continue
                
                answer.add(" ".join(puzzle))
        return list(answer)
                    