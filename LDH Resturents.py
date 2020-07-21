resturent1 = {
    "name": "The table by basant",
    "categories": ["North Indian", "Pzza", "Fast Food"],
    "time to diliver": "34 mins",
    "per person price": "₹ 250"

}
resturent2 = {
    "name": "Basant",
    "categories": ["North Indian", "Pizza", "Fast Food"],
    "time to diliver": "32 mins",
    "per person price": "₹ 200"

}
resturent3 = {
    "name": "Natural Soups & Shankes",
    "categories": ["Beverages", "Desserts", "South Indian", "Fast Food"],
    "time to diliver": "24 mins",
    "per person price": "₹ 150"

}
resturent4 = {
    "name": "B7 Restuarant",
    "categories": ["North Indian", "Biryani", "Chinese"],
    "time to diliver": "44 mins",
    "per person price": "₹ 250"

}
resturent5 = {
    "name": "Natural 2",
    "categories": ["North Indian", "Chinese", "Fast Food", "Italian", "Rolls"],
    "time to diliver": "27 mins",
    "per person price": "₹ 100"

}
resturent6 = {
    "name": "Baba Chicken",
    "categories": ["North Indian", "Mughlai", "chinese"],
    "time to diliver": "33 mins",
    "per person price": "₹ 350"

}
resturent7 = {
    "name": "Kathi Junction",
    "categories": ["Chinese", "Roll", "Fast Food"],
    "time to diliver": "47 mins",
    "per person price": "₹ 150"

}
resturent8 = {
    "name": "The table by basant",
    "categories": ["North Indian", "Pzza", "Fast Food"],
    "time to diliver": "34 mins",
    "recovered": 2538,
    "per person price": "₹ 250"

}
resturent9 = {
    "name": "The Burger Lab",
    "categories":  "Fast Food",
    "time to diliver": "51 mins",
    "per person price": "₹ 200"

}
resturent10 = {
    "name": "Ice Cream Studio",
    "categories": ["Ice Creams", "Desserts", "Sundaes"],
    "time to diliver": "35 mins",
    "per person price": "₹ 200"
}

resturents = [resturent1, resturent2, resturent3, resturent4, resturent5, resturent6,resturent7, resturent8, resturent9, resturent10]

print()

filter1 = input("Please Enter 1st Filter from [name | confirmed | categories | time to diliver | per person price]: ")
filter2 = input("Please Enter 2nd Filter from [name | confirmed | categories | time to diliver | per person price]: ")
filter3 = input("Please Enter 2nd Filter from [name | confirmed | categories | time to diliver | per person price]: ")

for i in range(0, len(resturents)):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("{}: {}\n{}: {}\n{}: {}".format(filter1.upper(), resturents[i][filter1], filter2.upper(), resturents[i][filter2],
                                          filter3.upper(), resturents[i][filter3]))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print()

name = input("Enter the name of Resturant to search: ")
for i in range(0, len(resturents)):

    print("Matching {} with {}".format(name, resturents[i]["name"]))

    if name.lower() == resturents[i]["name"].lower():
        print("State {} Found. Details are Below:".format(name))
        print(resturents[i])
        break
