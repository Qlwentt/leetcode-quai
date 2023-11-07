class SeatManager:

    def __init__(self, n: int):
        self.marker = 1
        self.available_seats = []


    def reserve(self) -> int:
        if self.available_seats:
            seat_number = heapq.heappop(self.available_seats)
            return seat_number
        seat_number = self.marker
        self.marker += 1
        return seat_number

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)