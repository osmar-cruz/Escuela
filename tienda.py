inventory = [
    {'category': 'tshirt', 'name': 'Leverkusen T-shirt',      'price': 20,  'tax_rate': 0.16},
    {'category': 'tshirt', 'name': 'Bayern Munich T-shirt',   'price': 22,  'tax_rate': 0.16},
    {'category': 'tshirt', 'name': 'Dortmund T-shirt',        'price': 18,  'tax_rate': 0.16},
    {'category': 'tshirt', 'name': 'RB Leipzig T-shirt',      'price': 25,  'tax_rate': 0.16},
    {'category': 'tshirt', 'name': 'Liverpool Champion',      'price': 30,  'tax_rate': 0.16},
    {'category': 'shoes',  'name': 'Adidas Predator',         'price': 100, 'tax_rate': 0.16},
    {'category': 'shoes',  'name': 'Nike Mercurial',          'price': 120, 'tax_rate': 0.16},
    {'category': 'shoes',  'name': 'Puma Future',             'price': 90,  'tax_rate': 0.16},
    {'category': 'shoes',  'name': 'Under Armour Clone',      'price': 110, 'tax_rate': 0.16},
    {'category': 'shoes',  'name': 'New Balance Furon',       'price': 95,  'tax_rate': 0.16},
]       #Diccionary list representing the inventory of the store
def show_inventory(inv): #Displays the inventory to the user
    print("Welcome to the T-shirt and Shoes store!")
    print("Here is our inventory:\n")

    print("T-shirts:")
    for idx, item in enumerate(inv):
        if item['category'] == 'tshirt':
            print(f"[{idx}] {item['name']}  ($ {item['price']})")

    print("\nShoes:")
    for idx, item in enumerate(inv):
        if item['category'] == 'shoes':
            print(f"[{idx}] {item['name']}  ($ {item['price']})")
    print()

def choose_item(inv): #Asks user to choose an item and validates input
    while True:
        choice = input("Enter the number of the item you want to buy: ")
        try:
            choice_i = int(choice)
            if 0 <= choice_i < len(inv):
                return inv[choice_i]
            else:
                print("That item number does not exist. Try again.")
        except ValueError:
            print("Please enter a valid integer index.")

def ask_quantity(): #Asks user for quantity and validates input
    while True:
        user_input = input("How many units do you want to buy? ")
        try:
            q = int(user_input)
            if q > 0:
                return q
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer number.")

def compute_discount(quantity):

    if quantity >= 15:
        print("You have a 25% discount.")
        return 0.25
    elif quantity >= 5:
        print("You have a 15% discount.")
        return 0.15
    else:
        print("You don't have any discount.")
        return 0.0

def calculate_totals(quantity, unit_price, tax_rate):
#It calculates subtotal, tax total, discount money, and final total
    subtotal = unit_price * quantity

    tax_total = unit_price * tax_rate * quantity

    discount_rate = compute_discount(quantity)
    discount_money = subtotal * discount_rate

    final_total = subtotal + tax_total - discount_money

    return subtotal, tax_total, discount_money, final_total

def print_receipt(
    product_name,
    quantity,
    unit_price,
    subtotal,
    tax_total,
    discount_money,
    final_total
):
    print("----- RECEIPT -----")
    print(f"Item: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price per unit: ${unit_price}")
    print(f"Subtotal: ${subtotal}")
    print(f"Taxes: ${tax_total}")
    print(f"Discount: ${discount_money}")
    print(f"TOTAL: ${final_total}")
    print("-------------------")


def main():
    # Show inventory to user
    show_inventory(inventory)

    #Ask user to choose item
    selected_item = choose_item(inventory)

    product_name = selected_item['name']
    unit_price = selected_item['price']
    tax_rate = selected_item['tax_rate']

    print(f"\nYou selected: {product_name} (${unit_price})")

    # Ask quantity
    quantity = ask_quantity()

    #Calculate totals
    subtotal, tax_total, discount_money, final_total = calculate_totals(
        quantity,
        unit_price,
        tax_rate
    )

    #Show totals to user
    print(f"\nThe total price is: ${final_total}")
    #Ask if user wants a receipt
    receipt_option = input("Do you want a receipt? (Y/N): ").strip().lower()

    if receipt_option == "y":
        email = input("Please enter your email: ")
        print_receipt(
            product_name,
            quantity,
            unit_price,
            subtotal,
            tax_total,
            discount_money,
            final_total
        )
        print(f"The receipt has been sent to {email}. Thank you for your purchase!")
    elif receipt_option == "n":
        print("Thank you for your purchase!")
    else:
        print("Invalid option. No receipt generated.")
main()
