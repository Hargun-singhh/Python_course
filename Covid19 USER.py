import requests
import json
import matplotlib.pyplot as plt
url = "https://api.covid19india.org/data.json"

response = requests.get(url)
covid_data = json.loads(response.text)

covid_cases_india = []
for i in range(0, len(covid_data["statewise"])):
    covid_cases_india.append(
        {
            "state": covid_data["statewise"][i]["state"],
            "active": covid_data["statewise"][i]["active"],
            "confirmed": covid_data["statewise"][i]["confirmed"],
            "deaths": covid_data["statewise"][i]["deaths"],
        }
    )

option1 = input("Please Enter 1st Filter from [active | confirmed | deaths | recovered | state]: ")
option2 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")
option3 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")

for i in range(0, len(covid_cases_india)):
    print("_--__--__--__--__--__--__--__--_")
    print("{}: {}\n{}: {}\n{}: {}".format(option1.upper(), covid_cases_india[i][option1], option2.upper(),
                                          covid_cases_india[i][option2],
                                          option3.upper(), covid_cases_india[i][option3]))
    print(covid_data["statewise"][i]["lastupdatedtime"], )
    print("_--__--__--__--__--__--__--__--_")
    print()


total_confirmed = []
for case in covid_cases_india:
    total_confirmed.append(int(case['confirmed']))

plt.plot(total_confirmed)
plt.show()

file = open("COVID19_DATA_STATE VISE.csv", "a")
file.write(str(covid_data["statewise"]))
print("Data Saved :)")
