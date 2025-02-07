class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors_to_balls = defaultdict(set)
        ball_to_color = {}
        answers = []
        for ball, color in queries:
            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                colors_to_balls[prev_color].remove(ball)
                if len(colors_to_balls[prev_color]) == 0:
                    del colors_to_balls[prev_color]
            colors_to_balls[color].add(ball)
            ball_to_color[ball] = color
            answers.append(len(colors_to_balls))
        return answers