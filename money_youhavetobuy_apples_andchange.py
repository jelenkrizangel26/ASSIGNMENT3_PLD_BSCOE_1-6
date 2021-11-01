# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def moneyAmnt():
    _money = int(input("How much money do you have to buy apples?: "))
    return _money

def priceApple():
    _priceAp = int(input("How much is an priceAppl?: "))
    return _priceAp

def ttlApples():
    _totalAp = moneyAm // applePrc
    return _totalAp

def Change():
    _chng = moneyAm % applePrc
    return _chng

def display(appleTtl, change):
    print(f"You can buy {appleTtl} apples and your change is {change} pesos.")

# steps
# 1. Ask for the amount of money you have then save the variable.
moneyAm = moneyAmnt()
# 2. Ask for the price of an apple then save the variable.
applePrc = priceApple()
# 3. Solve for total amount of apples you can bu then save the variable.
appleTtl = ttlApples()
# 4. Solve for the change then save the variable.
change = Change()
# 5. Display the total number of apples and the change.
display(appleTtl, change)
