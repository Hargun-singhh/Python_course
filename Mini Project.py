print("ORDER FOOD ONLINE FROM ZOMATO")
print("~+~~+~~+~~+~~+~~+~~+~~+~~+~~+~~+")
print("TIKKA JUNCTION")
print("~~~~~~~~~~~~~~")
print("TIME TO DELIVER = 33 MINS")
print("***+++***+++***+++***+++***+++***")
print("SAFETY MEASURES = 4.5 / 5")
print("***+++***+++***+++***+++***+++***")
products = {
    "kadhai paneer": 340,
    "dal makhani": 320,
    "soya chaap casala": 340,
    "veg soya chaap": 390,
    "afghani chaap tikka ": 330,
    "veg tandoori momos": 280,
    "better naan": 65,
    "tandoori roti": 30,
    "paneer tikka roll": 290,
    "romali roti": 35,
    "butter roti": 35,
    "atta lachha paratha": 55,
    "mineral water ": 49,
    "veg hot and sour soup": 140,
    "veg lemon coriander": 140,
    "veg manchow soup": 140,
    "veg sweet corn soup": 140,
    "veg talumein soup": 140,
    "mushroom malai tikka": 330,
    "mashroom tikka": 330,
    "paneer achari tikka": 330,
    "paneer kali mirch tikka": 330,
    "paneer lahsuni tikka": 330,
    "paneer malai tikka": 330,
    "paneer tikka": 330,
    "peri peri chaap tikka": 330,
    "paneer papdi": 330,
    "dahi ke sholey": 330,
    "dahi kebab": 330,
    "french fries": 220,
    "chilli mushroom": 330,
    "chilli paneer": 330,
    "crispy chilli potatoes": 310,
    "crispy honey chilli soya": 310,
    "honey chilli potatoes": 310,
    "manchurian dry": 330,
    "soya drums of heaven": 330,
    "spring roll": 310,
    "tandoori spring roll": 310,
    "soya schewan": 330,
    "crispy veg salt and pepper": 310,
    "pepricano roll": 310,
    "veg satay": 310,
    "dal dhaba": 320,
    "paneer  butter masala": 340,
    "paneer lababdar": 340,
    "shahi paneer ": 330,
    "paneer bhurji": 330,
    "moong dal tadka": 320,
    "mix veg": 340,
    "palak paneer ": 340,
    "paneer methi malai": 340,
    "malai kofta": 370,
    "chilly mushroom gravy": 350,
    "chilly paneer gravy": 350,
    "veg manchurian gravy": 350,
    "mixed veg in hot garlic sauce": 350,
    "plain rice": 200,
    "jeera rice": 230,
    "veg biryani": 320,
    "streamed rice": 190,
    "veg  chilli garlic rice ": 230,
    "veg hakka noodles": 230,
    "veg butter noodles": 250,
    "veg pan fried noodles": 250,
    "veg chopsuey": 290,
    "mushroom tikka roll": 290,
    "soya roll": 290,
    "veg singapore noodles": 340,
    "paneer tikka paratha roll": 230,
    "kurkure veg momos": 280,
    "veg fried momos": 260,
    "veg honey chilli toss momos": 280,
    "veg streamed momos": 260,
    "cream roti": 40,
    "masala roti": 65,
    "gralic roti": 45,
    "naan": 55,
    "masala naan": 65,
    "butter naan": 65,
    "mirchi paratha": 65,
    "garlic naan": 75,
    "paneer naan": 85,
    "paneer paratha": 75,
    "blue lagoon": 199,
    "virjin mojito": 199,
    "kiwi blast": 199,
    "red bull": 199,
    "masala papad": 140,
    "peanut papad": 200,

}

cart = []
choice = "yes"

quantity = 1

while choice == "yes":
    product = input("Enter Dish of Your Choice:")
    quantity = int(input("Enter QUANTITY OF Dish:"))
    cart.append(products[product])
    choice = input("Would you like to add another dish (yes/no)")

print("Your Cart [", len(cart), "]:")
print(cart)


total = 0

delivery = 50

for price in cart:
    total = total + price * quantity

print("TOTAL:", total)

promoCode = input("Enter the Promo Code: ")

if total >= 500:


    if promoCode == "EATREPEAT":
        discount = 0.40 * total

        if discount >= 200:
            discount = 200

        amountToPay = total - discount + delivery
        print("EATREPEAT Applied")
        print("Discount of \u20b9", discount, "applied. Please pay total including delivery charges : \u20b9", amountToPay)
promoCode = input("Enter the Promo Code: ")
if total >= 1000:

    if promoCode == "TRYNOW":
        discount = 0.50 * total

        if discount >= 400:
            discount = 400

        amountToPay = total - discount + delivery

        print("TRYNOW Applied")
        print("Discount of \u20b9", discount, "Applied. Please Pay Total Incluing Delivery Charges: \u20b9", amountToPay)

    else:
        print("No PromoCode Applicable")
        print("Please Pay: \u20b9", total)