text_line = input()
orders = dict()
while not text_line == "buy":
    name, price, quantity = text_line.split(" ")
    if name not in orders.keys():
        orders[name] = [price, int(quantity)]
    else :
        orders[name] = [price, float(orders[name][1]) + int(quantity)]

    text_line = input()
for order, [price,quantity] in orders.items() :
    print(f"{order} -> {(float(price) * int(quantity)):.2f}")
