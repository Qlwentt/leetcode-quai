class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_map = collections.defaultdict(lambda : {'total_score': 0, 'scores': []})
        
        for student, score in items:
            heap = score_map[student]['scores']
            heapq.heappush(heap, score)
            score_map[student]['total_score'] += score
            
            if len(heap) > 5:
                decr_score = heapq.heappop(heap)
                score_map[student]['total_score'] -= decr_score
                
        answer = []
        for student, score_data in score_map.items():
            answer.append([student, score_data['total_score'] // 5])
            
        answer.sort()
        return answer
            
        
        
        