class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        strobo = {
            "0" : "0",
            "1" : "1",
            "6" : '9',
            "8" : '8',
            "9" : '6'
        }
        
        def buildStrobo(n, needZero):
            answers = []
            if n == 1:
                for s in strobo:
                    if s == strobo[s]:
                        answers.append(s)
                return answers
            if n == 2:
                for s in strobo:
                    if s != "0" or needZero:
                        answers.append(s+strobo[s])
                return answers
            
            prevAnswers = buildStrobo(n-2, True)
            
            for answer in prevAnswers:
                for s in strobo:
                    if s != "0" or needZero:
                        answers.append(s+answer+strobo[s])
            return answers
        return buildStrobo(n, False)
                
                