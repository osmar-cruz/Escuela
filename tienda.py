#Arithmetics operators.
price=20
taxes=0.16
tshirts = ['leverkusen tshirt, liverpool tshirt, madrid tshirt, barcelona tshirt, chivas tshirt']
size = ['XS', 'S', 'M', 'L', 'XL']
for tshirt in [tshirts]:
    print(tshirt)
for size in [size]
    print(size)

def sizes(size):
    if size == 'XS':
        size += 5
    elif size == 'S':
        size += 7
    elif size == 'M':
        size += 9
    if size == 'L':
        size += 12
    elif size == 'XL':
        size +=14
        
def compute_discount(quantity): #I define a function to compute the discount based on the quantity of tshirts bought
    if quantity == 5:
        print("You have a 15% discount")
        return 0.15 #if the quantity is 5, the discount is 15%
    elif quantity >= 15:
        print("You have a 25% discount")
        return 0.25 #if the quantity is 15 or more, the discount is 25%
    else:
        print("You don't have any discount")
        return 0 #if the quantity is less than 5, there is no discount

def shopping():
    while True:
    quantity = (int(input ("How many tshirts do you want to buy?")))

    size = (input('Please pick a size: ')) #This just Make the user to pick a size
    
    total_taxes = quantity * taxes
    print(f"You have to pay", total_taxes, "in taxes for each tshirt")

    discount = compute_discount(quantity) * price * quantity #I call the function to compute the discount and multiply it by the price and quantity to get the total discount amount
    total_price = (price * quantity) + total_taxes - discount 
    #In this line I calculate the total price with the formula (price * quantity) + total_taxes - discount, and I store it in the variable total_price
    print(f"The total price is: ", total_price)

    receipt_option = input("Do you want a receipt? (Y/N): ").lower() #I ask the user if they want a receipt and convert the answer to lowercase
    if receipt_option == "y": #If the answer is yes, I print the receipt
        while receipt_option.lower() == "y":
             receipt_option = input("Please enter your email: ")
            
        print("----- RECEIPT -----")
        print(f"Quantity: {quantity}")
        print(f"Price per tshirt: {price}")
        print(f"Taxes: {total_taxes}")
        print(f"Discount: {discount}")
        print(f"Total price: {total_price}")
        print("-------------------")    
        print("The receipt has been sent to your email, Thank you for your purchase!")
    elif receipt_option.lower() == "n":
        print("Thank you for your purchase!")
    else:
        print("Please insert a letter!") #If the answer is no, I thank the user for their purchase

    another_purchase = print(input('Would you like to do another purchase? (y/n)'))
    if another_purchase == 'y':
        return True
    else:
        print('Thanks for visiting us!')
        return False
shopping()
