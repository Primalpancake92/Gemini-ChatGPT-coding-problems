class Inventory:
    def __init__(self):
        self.inventory = []
        
    
    def add_item(self, item_code: str, name: str, price: float, quantity: int):
        # checks if the item exists in the inventory
        for item in self.inventory:
            # conditional that states if found then
            if item_code == item[0]:
                # update the quantity
                item[3] = quantity
                return
        # adds item in the inventory of the item is not found
        self.inventory.append([item_code, name, price, quantity])
        

    def remove_item(self, item_code: str):
        #checks if the item exists in the inventory
        for item in self.inventory:
            # condition that states if found then
            if item[0] == item_code:
                # remove the item based on the item code
                self.inventory.remove(item)
                # return right after
                return
        # if not found then print the following
        print("Item not found in inventory.")
    
    
    def update_quantity(self, item_code: str, quantity: int):
        # checks if the item exists in the inventory 
        for item in self.inventory:
            # condition if the item is found
            if item[0] == item_code:
                # updates quantity
                item[3] = quantity
                # return
                return
        # if not found then print the following
        print("Item not found in inventory.")
    
    
    def check_stock(self, item_code: str):
        # checks if the item exists in the inventory
        for item in self.inventory:
            # condition if the item is found
            if item[0] == item_code:
                # returns the item quantity
                return item[3]
        # if not found then return -1
        return -1
        
    
    def print_inventory(self):
        # iterates through every item in the inventory
        for item in self.inventory:
            # prints the items details 
            print(f"\nItem code: {item[0]}\nName: {item[1]}\nPrice: {item[2]}\nQuantity: {item[3]}\n")


if __name__ == "__main__":
    # Creating an inventory object
    inventory = Inventory()

    # Adding items
    inventory.add_item('001', 'Apple', 0.5, 50)
    inventory.add_item('002', 'Banana', 0.3, 100)

    # Checking stock
    print(inventory.check_stock('001'))  # Output: 50

    # Updating quantity
    inventory.update_quantity('001', 25)  # Updates Apple quantity to 25

    # Printing inventory
    inventory.print_inventory()

    # Removing an item
    inventory.remove_item('002')

    # Checking stock for removed item
    print(inventory.check_stock('002'))  # Output: -1 (since Banana was removed)
