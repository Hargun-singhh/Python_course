import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Dish:

    def __init__(self, name, phone, email, Pickup, Drop):
        self.name = name
        self.phone = phone
        self.email = email
        self.PickUp = Pickup
        self.Drop = Drop

    def Dish(self):
        print("-------------------------------------")
        print("|  {}  |  {}  |  {}  |  {}  |  {}  |".format(self.name, self.phone, self.email, self.PickUp, self.Drop))
        print("-------------------------------------")

    def to_dictionary(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'Pickup': self.PickUp,
            'Drop': self.Drop
        }


class Menu:

    def __init__(self, Cab_type, Pickup_location, Drop_location, dishes):
        self.Cab_type = Cab_type
        self.Pickup_location = Pickup_location
        self.Drop_location = Drop_location
        self.dishes = dishes

    def show_menu(self):
        print("^^^^^CAB DETAILS^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.Cab_type, self.Pickup_location, self.Drop_location))
        print("-------------------------------------")

        print("DISHES: ")
        for dish in self.dishes:
            dish.show_dish()

    def to_dictionary(self):
        return {
            'Cab_type': self.Cab_type,
            'Pickup_location': self.Pickup_location,
            'Drop_location': self.Drop_location
        }


class Restaurant:

    def __init__(self, User_name, User_phone, User_email, menu):
        self.User_name = User_name
        self.User_phone = User_phone
        self.User_email = User_email
        self.menu = menu

    def show_restaurnat(self):
        print("^^^^^^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.User_name, self.User_phone))
        print("|  {}  |".format(self.User_email))
        print("-------------------------------------")

        self.menu.show_menu()

    def to_dictionary(self):
        return {
            'name': self.User_name,
            'phone': self.User_phone,
            'email': self.User_email,
        }

def main():

    # Intialize Firebase App which serves as connection to the Firebase for our Usage :)
    cred = credentials.Certificate('Noob.json')  # PS: firebase-key.json to be downloaded aas a file and to be saved in your python project
    firebase_admin.initialize_app(cred)
    print("Firebase Initialized")

    restaurant = Restaurant(
        User_name="Hargun",
        User_phone="+91 99999 66666",
        User_email="hargunsingh14.hs@gmail.com",
        menu=Menu(
            Cab_type="mini ola",
            Pickup_location="Rolex Clothing",
            Drop_location="B.C.M School",
            dishes=[
                Dish(name="Hargun", phone=625464444848, email="har@gmail.com", Pickup="Rolex clothing",
                     Drop="B.C.M School"),
                Dish(name="HArjas", phone=1548644848, email="har@gmail.com", Pickup="Trend Plus", Drop="Auribases"),
            ]
        )
    )

    # Get the data as Dictionary from Object
    data_to_save = restaurant.to_dictionary()
    print(data_to_save)

    menu_data = restaurant.menu.to_dictionary()
    print(menu_data)

    dishes = restaurant.menu.dishes


    db = firestore.client()

    for dish in dishes:
        dish_data = dish.to_dictionary()
        db.collection('User').document('Request')\
            .collection('User_Details').document(dish.name).set(dish_data) # set will also insert/update the data for us :)
        print(dish.name, "Saved")
    print("Data Saved :)")




if __name__ == '__main__':
    main()
