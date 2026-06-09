#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discounted_total = self.total * (100 - self.discount) / 100
        self.total = int(discounted_total) if discounted_total.is_integer() else discounted_total
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            self.total = 0
            self.items = []
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        if self.total < 0:
            self.total = 0

        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
