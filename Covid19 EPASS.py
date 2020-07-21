import datetime as dt  # with alias

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Noob.json")
firebase_admin.initialize_app(cred)

print("~~+~~++~CONNECTING TO SERVER FOR Covid19 Epass~+~~++~~")
print("~~+~~++~CONNECTING TO SERVER FOR Covid19 Epass~+~~++~~")
print("~~+~~++~CONNECTING TO SERVER FOR Covid19 Epass~+~~++~~")
print("<<<<<<<<CONNECTED  TO SERVER FOR Covid19 Epass>>>>>>>>")

today = dt.datetime.today()


class Pass:

    def __init__(self, name, phone, email, from_location, to_location, family_members, adrress, vehicle_number,
                 nationality, id, District, Pass_Type, From_Date, To_Date):
        self.name = input("ENTER YOUR NAME:")
        self.phone = input("ENTER YOUR PHONE NUMBER:")
        self.email = input("ENTER YOUR EMAIL:")
        self.from_location = input("ENTER ORIGIN:")
        self.to_location = input("ENTER DESTINATION:")
        self.family_members = input("ENTER FAMILY MEMBERS:")
        self.adrress = input("ENTER YOUR ADRRESS:")
        self.vehicle_number = input("ENTER VEHICLE:")
        self.nationality = input("ENTER NATIONALITY:")
        self.id_Type = input("CHOOSE ID TYPE [AADHAR CARD | DRIVING LICENCE |  PAN CARD  ]: ")
        self.District = input("ENTER YOUR DISTRICT:")
        self.Pass_Type = input("CHOOSE PASS TYPE [LOCAL | INTER DISTRICT |  INTER STATE  ]: ")
        self.From_Date = today
        self.To_Date = "12-August-2020"

    def show(self):
        pass


def main():
    pRef = Pass("self.name", "self.phone", 'self.email', 'self.from_location', 'self.to_location',
                'self.family_members', 'self.adrress', 'self.vehicle_number', 'self.nationality', 'self.id',
                'self.District', 'self.Pass_Type', 'self.From_Date', 'self.To_Date')

    # To save data in firebase firestore collection, document has to be a dictionary like below :)
    pRef_dictionary = pRef.__dict__

    # db is reference variable which refers to firestore database from our python program
    db = firestore.client()

    db.collection("passes").document(pRef.name).set(pRef_dictionary)  # Insert and Update Both :)
    print("YOUR COVID19 Epass HAS BEEN SUCCESFULLY SUBMITED:")
    # print("DATA UPDATED :)")
    # db.collection("passes").document("987651234").delete()
    # print("DATA DELETED")

    # Read all the documents from Collection
    # documents = db.collection("passes").get()
    # for document in documents:
    #     print(document.id, document.to_dict())
    # Read Single Document
    # document = db.collection("passes").document("9876512345").get()
    # print(document.id, document.to_dict())


if __name__ == '__main__':
    main()