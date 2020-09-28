class CoffeeMachine:
    # Amount of products
    def __init__(self):
        self.water = 400  # ml
        self.milk = 540  # ml
        self.beans = 120  # grams
        self.cups = 9
        self.money = 550  # $

    # Machine's state
    def state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    # Buy action
    def buy(self, coffee_name):
        if coffee_name == "1":  # If user want to buy espresso
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            else:
                if self.water < 250:
                    print("Sorry, not enough water\n")
                if self.beans < 16:
                    print("Sorry, not enough coffee beans\n")
                if self.cups < 1:
                    print("Sorry, not enough cups\n")
        elif coffee_name == "2":  # If user want to buy latte
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            else:
                if self.water < 350:
                    print("Sorry, not enough water\n")
                if self.milk < 75:
                    print("Sorry, not enough milk\n")
                if self.beans < 20:
                    print("Sorry, not enough coffee beans\n")
                if self.cups < 1:
                    print("Sorry, not enough cups\n")
        elif coffee_name == "3":  # If user want to buy cappuccino
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            else:
                if self.water < 200:
                    print("Sorry, not enough water\n")
                if self.milk < 100:
                    print("Sorry, not enough milk\n")
                if self.beans < 12:
                    print("Sorry, not enough coffee beans\n")
                if self.cups < 1:
                    print("Sorry, not enough cups\n")

    # Fill action
    def fill(self):
        self.water += int(input("\nWrite how many ml of water do you want to add: \n"))
        self.milk += int(input("Write how many ml of milk do you want to add: \n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: \n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: \n"))

    # Take action
    def take(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def coffee(self):
        coffee_name = input(
            "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        self.buy(coffee_name)
        if coffee_name == "back":
            pass

    # Start
    def main(self):
        while True:
            action = input("\nWrite action (buy, fill, take, remaining, exit): \n")
            if action == "buy":
                self.coffee()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.state()
            elif action == "exit":
                break


CoffeeMachine().main()
