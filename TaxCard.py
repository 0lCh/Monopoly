from Card import Card


class TaxCard(Card):
    def __init__(self, name, id, tax):
        self.name = name
        self.id = id
        self.tax = tax
