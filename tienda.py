#Arithmetics operators.
price=20
taxes=0.16
tshirts=["leverkusen tshirt","liverpool tshirt","madrid tshirt", "barcelona tshirt", "chivas tshirt"]
for tshirt in [tshirts]:
    print("-", tshirt)
quantity = (int(input ("How many tshirts do you want to buy?")))
total_taxes = quantity * taxes
print(f"You have to pay", total_taxes, "in taxes for each tshirt")
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
discount = compute_discount(quantity) * price * quantity #I call the function to compute the discount and multiply it by the price and quantity to get the total discount amount
total_price = (price * quantity) + total_taxes - discount 
"""In this line I calculate the total price with the formula (price * quantity) + total_taxes - discount, and I store it in the variable total_price
i gave a variable discount to store the discount value for the clients, if you buy 15 or more tshirts you have a 25% discount, if you buy 5 tshirts you have a 15% discount, 
if you buy less than 5 tshirts you don't have any discount"""

print(f"The total price is: ", total_price)
