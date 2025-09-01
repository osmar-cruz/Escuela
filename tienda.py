#Arithmetics operators.
price=20
taxes=0.16
tshirts=["leverkusen tshirt","liverpool tshirt","madrid tshirt", "barcelona tshirt", "chivas tshirt"]
for tshirt in [tshirts]:
    print("-", tshirt)
quantity = (int(input ("How many tshirts do you want to buy?")))
total_taxes = quantity * taxes
print(f"You have to pay", total_taxes, "in taxes for each tshirt")
if quantity == 5:
    print("You have to pay 16 in taxes, and you have 15% discount")
elif quantity >=15:
    print("You have to pay 16 in taxes, and you have 25% discount")
    discount = int(input("How much is your discount?: "))
elif quantity < 5:
    print("You have to pay 0 in taxes")
total_price = (price * quantity) + total_taxes - discount 
"""In this line I calculate the total price with the formula (price * quantity) + total_taxes - discount, and I store it in the variable total_price
i gave a variable discount to store the discount value for the clients, if you buy 15 or more tshirts you have a 25% discount, if you buy 5 tshirts you have a 15% discount, 
if you buy less than 5 tshirts you don't have any discount"""
print(f"The total price is: ", total_price)