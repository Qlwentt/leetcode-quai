class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        plants = [0] + plants + [0]
        cur_capacity = capacity
        answer = 0
        for i in range(len(plants)-1):
            answer += 1 if i else 0
            cur_capacity -= plants[i]
            if cur_capacity < plants[i+1]:
                answer += i * 2
                cur_capacity = capacity
        return answer
        