class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # power = damage
        # maxPower = max(power)
        # def canWin(health, armor):
        #     for p in power:
        #         if p == maxPower:
        #             health -= (p - armor) if p > armor else 0
        #             armor = 0
        #         else:
        #             health -= p
        #         if health <= 0:
        #             return False
        #     return True
        # low = 0
        # high = sum(power)
        # while low <= high:
        #     mid = (low + high) // 2
        #     if canWin(mid,armor):
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return low
        resist = min(max(damage), armor)
        return sum(damage) + 1 - resist