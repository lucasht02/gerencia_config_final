class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self, payment_method):
        return payment_method.charge(self.amount)

    def validate_card(self, card_number):
        return isinstance(card_number, str) and len(card_number) == 16