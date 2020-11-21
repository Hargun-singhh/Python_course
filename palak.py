print("~+~~+~~+~~+~~+~~+~~+~~+~~+~~+~~+")
print("DINE & DIVINE ")
print("~~~~~~~~~~~~~~")
print("SAFETY MEASURES = 4.5 / 5")
print("***+++***+++***+++***+++***+++***")
print("|||SURPLUS FOOD FOR LESS PRICE|||")
print("__--__--__--__--__--__--__--__")
print()
print( "Dal Makhani(Half Plate) ₹130 ")
print( "butter roti(4) ₹90 ")
print( "veg sweet corn soup(2 CUPS ) ₹90 ")
print( "paneer malai tikka(Half Plate) ₹150 ")
print( "paneer tikka( 7 Pieces) ₹170 ")
print( "spring roll(5 Rolls) ₹100 ")
print( "paneer  butter masala(Half Plate) ₹180 ")
print( "shahi paneer (Two Plate) ₹170 ")
print( "mix veg(Half Plate) ₹90 ")
print( "veg hakka noodles(Half Plate) ₹180 ")
print( "veg fried momos(5 Pieces) ₹90 ")
print( "Naan (6 Naans ) ₹110 ")
print("veg manchurian gravy(Half Plate) ₹190")
print("plain rice( Quater Plate )₹150")
print()
print("++++++++++++++++++++++++++++++++++++")
print()




products = {
    "dal makhani": 130,
    "butter roti": 35,
    "veg sweet corn soup": 90,
    "paneer malai tikka": 150,
    "paneer tikka": 170,
    "spring roll": 100,
    "paneer  butter masala": 180,
    "shahi paneer ": 170,
    "mix veg": 90,
    "veg manchurian gravy": 190,
    "plain rice ": 150,
    "veg hakka noodles": 180,
    "veg fried momos": 90,
    "naan": 110,

}

cart = []
choice = "yes"


while choice == "yes":
    product = input("Enter Dish of Your Choice:")
    cart.append(products[product])
    choice = input("Would you like to add another dish (yes/no)")

print("___________________________________________")
print("YOUR FOOD ORDER IS PLACED SUCCESFULLY & FOOD WILL BE DELIVER BY HOTEL")
print("____________________________________________")
print("Your Cart [", len(cart), "]:")
print(cart)


total = 0


for price in cart:
    total = total + price

print("TOTAL BILL:", total)


