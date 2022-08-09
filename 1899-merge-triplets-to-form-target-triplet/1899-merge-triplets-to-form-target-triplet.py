class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        srcTriplets = []
        for triplet in triplets:
            a , b, c = triplet
            if (a > target[0] or
                b > target[1] or
                c > target[2]):
                continue
            srcTriplets.append(triplet)
        found = [False] * 3
        for triplet in srcTriplets:
            a, b, c = triplet
            if a == target[0]:
                found[0] = True
            if b == target[1]:
                found[1] = True
            if c == target[2]:
                found[2] = True
                
        return found[0] == True and found[1] == True and found[2] == True