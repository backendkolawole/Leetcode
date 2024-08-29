class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_sum = 0
        max_score = 0
        window_size = len(cardPoints) - k

        total_points = sum(cardPoints)
        
        for i in range(window_size):
            window_sum += cardPoints[i]

        max_score = total_points - window_sum

        for i in range(window_size, len(cardPoints)):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            score = total_points - window_sum
            max_score = max(max_score, score)

        return max_score

        