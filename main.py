class Bakery:

    def __init__(self):

        #(price, inventory)        
        self.menu = {
            "banana nut pound cake": (4.00, 30),
            "coffee crumb cake": (4.00, 40),
            "chocolate chip cookie": (4.25, 20),
            "cranberry walnut scone": (4.00, 30),
            "croissant":(4.00, 20),
            "chocolate croissant": (4.50, 10)
            }

        self.sale = 0.00

    def display_menu(self):
        print("Bakery menu:")
        for item, (price, inventory) in self.menu.items():
            print(f"{item}: ${price:.2f}, Inventory: {inventory}")
            
    
    def place_order(self):
        while True:
            order = input("Enter the item you want to purchase (or 'done' to finish): ")
            if (order.lower() == "done"):
                break
            if order in self.menu:
                quantity = int(input(f"How many {order}s would you like to order: "))
                price, inventory = self.menu[order]
                if (inventory >= quantity):
                    self.menu[order] = (price, inventory - quantity)
                    self.sale += price * quantity
                    print(f"Order placed: {quantity} {order}(s).")
                else:
                    print(f"Sorry, we only have {inventory} {order}(s) in stock.")
            else: print(f"Sorry, {order} is not on the menu")

    def total_sales(self):
        print(f"Total Sale: {self.sale}")

    def manage_inventory(self):
        item_name = input("Enter the item you want to manage: ")

        if item_name in self.menu:
            price, inventory = self.menu[item_name]
            while True:
                try:
                    quantity = int(input(f"Enter the new inventory amount for {item_name}: "))
                    self.menu[item_name] = (price, quantity)
                    print(f"The new inventory for {item_name} has been updated to {quantity}")
                    break
                except ValueError:
                    print("Please enter a valid integer for the inventory.")
        else:
            print(f"Sorry, {item_name} is not on the menu")



bakery = Bakery()

def main():
    print("Python Coffee Inc.")
    while True:
        user_input = int(input("""1. Display menu
2. Place Order
3. View Total Sales
4. Manage Inventory
5. Exit
Enter your choice: """))
        if (user_input == 5):
            print("Thank you for using Elias Bakery Mangement System! Have a good day!")
            break
        elif (user_input == 1):
            bakery.display_menu()
        elif (user_input == 2):
            bakery.place_order()
        elif(user_input == 3):
            bakery.total_sales()
        elif(user_input == 4):
            bakery.manage_inventory()
        else:
            print("Please enter a valid choice!")
    


main()