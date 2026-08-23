def calculate_pizza_price(size):
    prices = {"small": 800,
              "medium": 1100,
              "large": 1500}
    return prices[size]
 
def apply_discount(price, coupon):
    if coupon == "SAVE10":
        return price - (price * 0.10)
    return price
 
def add_tax(price):
    return price + (price * 0.05)


# UNIT TEST: one function, alone
assert apply_discount(1000, "SAVE10") == 909
assert apply_discount(1000, "") == 1000
assert apply_discount(500, "FAKE99") == 500
 
print("Stop 1: unit tests passed!")
