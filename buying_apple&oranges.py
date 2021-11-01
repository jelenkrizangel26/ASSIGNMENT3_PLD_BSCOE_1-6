# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def showPriceAp():
    _PriceAP = 20
    print(f"The price of an apple is {_PriceAP} pesos.")
    return _PriceAP

def showPriceOr():
    _PriceOR = 25
    print(f"The price of an orange is {_PriceOR} pesos.")
    return _PriceOR

def amountAP():
    _AmountAP = int(input("How many apples will you buy? "))
    return _AmountAP

def amountOr():
    _AmountOr = int(input("How many orange will you buy? "))
    return _AmountOr

def totalP():
    _TPofApple = applePrice*appleQuantity
    _TPofOrange = orangePrice*orangeQuantity
    _TotalPrice = _TPofApple + _TPofOrange
    return _TotalPrice

def display(TtlPrice):
    print(f"The total amount is {TtlPrice} pesos. ")




# steps
# 1. Ask how many apples you want to buy then save the variable.
appleQuantity = amountAP()
# 2. Ask how many oranges you want to buy then save the variable.
orangeQuantity = amountOr()
# 3. Show the price of an apple then set as a variable.
applePrice = showPriceAp()
# 4. Show the price of an orange then set as a variable.
orangePrice = showPriceOr()
# 5. Solve for the total price then save to variable.
ttlPrice = totalP()
# 6. Display the total price.
total = display(ttlPrice)

