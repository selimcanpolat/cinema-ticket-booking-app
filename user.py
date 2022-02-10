class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        card.checkout(seat.get_price())
        seat.occupy()
