class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        answer = sorted([(rating,id_) for id_, rating, vegan_friendly, price, distance in restaurants if price <= maxPrice and distance <= maxDistance and vegan_friendly == (veganFriendly if veganFriendly == 1 else vegan_friendly)], reverse = True)
        return [id_ for rating,id_ in answer]