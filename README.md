# Escuela
Clase de Pensamiento Computacional para Ingenieria 1er Semestre.

Proyecto: Tienda en linea de camisetas de futbol.
Se me hace interesante el hecho de las camisetas de futbol y el como se maneja el sistema.
Siento que el algoritmo puede variar bastante dependiendo de lo que se busque o cosas asi.
Al igual siento que me ayudara de manera logica el como se manejan las cosas.
Algorithm: T-Shirt and Shoes Store

1.  Display a welcome message and the full inventory:
        - Divide products into two sections:
              a) T-shirts
              b) Shoes
        - Show each product with a number index and its price.

2.  Ask the user to enter the number of the item they want to buy:
        - Validate that the input is an integer and exists in the inventory.
        - If the number does not exist, ask again until a valid one is entered.

3.  Store the selected item information:
        - Product name
        - Unit price
        - Tax rate (tax_rate)

4.  Ask the user for the quantity of items to purchase:
        - Validate that the input is a positive integer greater than 0.
        - If not, ask again until a valid quantity is entered.

5.  Calculate the monetary values of the purchase:
        - subtotal ← unit_price × quantity
        - tax_total ← unit_price × tax_rate × quantity
        - discount_rate ← compute_discount(quantity)
        - discount_amount ← subtotal × discount_rate
        - final_total ← subtotal + tax_total − discount_amount

6.  Display the final total amount to the user.

7.  Ask the user if they want a receipt (Y/N):
        - If the answer is "Y" or "y":
              a) Ask for the user’s email.
              b) Print the receipt showing:
                     • product name  
                     • quantity  
                     • unit price  
                     • subtotal  
                     • taxes  
                     • discount  
                     • final total  
              c) Display a confirmation message indicating that the receipt was sent.
        - If the answer is "N" or "n":
              a) Display a thank-you message.
        - Otherwise:
              a) Display a message indicating an invalid option.

8.  End of the program.
