class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = collections.defaultdict(set)
        for user, minute in logs:
            user_minutes[user].add(minute)
        answer = [0] * (k+1)
        for user, minutes in user_minutes.items():
            answer[len(minutes)] += 1
            
        return answer[1:]