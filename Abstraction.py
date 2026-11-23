#Food Delivery App Using Abstraction
from abc import ABC, abstractmethod

class Food_delivery(ABC): #parent class
    
    @abstractmethod
    def place_order(self,food):
        pass

    @abstractmethod
    def calculate_bill(self, price):
        pass

class Zomato(Food_delivery): #child class

    def __init__(self):
        self.menu = {
            1: ("Pizza",200),
            2: ("Burger",200),
            3: ("French Fries",150),
            4: ("Coke",80),
            5: ("Burrito",250)
            }
        self.orders = []

    def place_order(self):
        print("\n*******FOOD MENU********")

        for key,value in self.menu.items():
            print(key,".",value[0],"Rs.",value[1])

        while True:
            choice = int(input("\nEnter your Food choice( 0 to Finish):"))
            if choice == 0:
                break
            if choice in self.menu:
                quantity = int(input("Enter the quantity:"))

                if quantity <= 0:
                    print("Enter valid Quantity!")
                    continue

                food = self.menu[choice][0]
                price = self.menu[choice][1]

                amount = price * quantity
                self.orders.append((food, quantity, amount))

                print( food," added to order")
            else:
                print("Invalid food choice, Try Again!")
                
    
    def calculate_bill(self):

        total = 0

        print("\n------ YOUR BILL ------")

        if len(self.orders) == 0:
            print("No orders placed!")

        else:
            for food, quantity, amount in self.orders:

                print(food, "x", quantity, "=", amount)

                total += amount

            delivery_charge = 20

            if total >= 1000:
                discount = total * 5 / 100
            else:
                discount = 0

            final_total = total + delivery_charge - discount

            print("----------------------")
            print("Food Total =", total)
            print("Delivery Charge =", delivery_charge)
            print("Discount =", discount)
            print("Final Total =", final_total)

            print("Thank you for ordering!")    

order = Zomato()
order.place_order()
order.calculate_bill()

    
            
        
