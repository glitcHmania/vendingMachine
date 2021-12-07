wallet = int(input("Determine your balance: "))
stock = [3,2,4,1,1]
provisions = ["Coke", "Chocolate", "Candy", "Cracker", "Chips"]
prices = [8,5,4,7,9]
def getInfo3():
    global info3
    info3 = str(input("Would you like anything else? (Y/N): ")).upper()
def infoPrinter():
    print("-"*100)
    print("Provision: "+info1.upper())
    print("Price :" +" "+ "$"+ str(prices[int(provisions.index(info1))]))
    print("Stock: "+" "+str(stock[int(provisions.index(info1))]))
    print(f"Balance: ${wallet}")
    print(f"Would you like to pay ${prices[int(provisions.index(info1))]}? (Y/N): ")
def zeroPrinter():
    print("-"*100)
    print("New Balance: 0")
    print("-"*100)
    print("*** Exit successful. ***")
    print("-"*100)
def negativePrinter():
    print("-"*100)
    print("*** You don't have enough money. ***")
    print("-"*100)
    print("*** Exit successful. ***")
    print("-"*100)
def oosPrinter():
    print("-"*100)
    print("Not enough stock.")
    print("-"*100)
def exitPrinter():
    print("-"*100)
    print("*** Exit successful. ***")
    print("-"*100)
def invalidPrinter():
    print("-"*100)
    print("*** Invalid answer. ***")
    print("-"*100)
def vendingMachine():
    global wallet
    print("-"*100)
    i = 0
    print("Welcome to Vending Machine!")
    print("-"*100)
    print(f"Balance: ${wallet}")
    print("-"*100)
    while i<5:
        print(i+1,"-",provisions[i])
        i +=1 
    print("-"*100)
    print("*** Type 'Exit' to exit ***")
    global info1
    info1 = str(input("Please type the name of the provision you want to pick: ")).capitalize()
    print("-"*100)
    if info1 in provisions:
        infoPrinter()
        answer = input("Answer: ").upper()
        if answer == "Y":
            wallet -= prices[int(provisions.index(info1))]
            stock[int(provisions.index(info1))] -= 1
            if wallet == 0:
                zeroPrinter()
                return None
            elif wallet < 0:
                negativePrinter()
                return None
            if stock[int(provisions.index(info1))] <0:
                oosPrinter()
                getInfo3()
                global info3
                if info3 == "Y":
                    vendingMachine()
                elif info3 == "N":
                    exitPrinter()
                    return None
                else:
                    invalidPrinter()
                    vendingMachine()
            if wallet < 0:
                return None
            print(f"Balance: ${wallet}")
            print("-"*100)
            getInfo3()
            if info3 == "Y":
                vendingMachine()
            elif info3 == "N":
                exitPrinter()
                return None
            else:
                invalidPrinter()
                vendingMachine()
        else:
            getInfo3()
            if info3 == "Y":
                vendingMachine()
            elif info3 == "N":
                exitPrinter()
                return None
            else:
                invalidPrinter()
                vendingMachine()
    elif info1 == "Exit":
        exitPrinter()
        return None
    else:
        invalidPrinter()
        vendingMachine()
vendingMachine()
