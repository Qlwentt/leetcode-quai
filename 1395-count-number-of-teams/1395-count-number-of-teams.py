class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        #[2,5,3,4,1]
        answer = 0

        # increasing = [3,0,1,0,0]
        # decreasing = [1,3,1,1,0]
        
        increasing = [0] * len(ratings)
        decreasing = [0] * len(ratings)
        
        for i in range(len(ratings)):
            for j in range(i+1, len(ratings)):
                increasing[i] += ratings[j] > ratings[i]
                decreasing[i] += ratings[j] < ratings[i]
        
        for i in range(len(ratings)):
            for j in range(i+1, len(ratings)):
                if ratings[j] > ratings[i]:
                    answer += increasing[j]
                elif ratings[j] < ratings[i]:
                    answer += decreasing[j]
                    
        return answer
        
        
        