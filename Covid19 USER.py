import requests
import json

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
            "lastupdatedtime": covid_data["statewise"][i]["deaths"],
        }
    )

filter1 = input("Please Enter 1st Filter from [active | confirmed | deaths | recovered | state]: ")
filter2 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")
filter3 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")

for i in range(0, len(covid_cases_india)):
    print("~~+~~++~~+~~++~~+~~++~~+~~++~~")
    print("{}: {}\n{}: {}\n{}: {}".format(filter1.upper(), covid_cases_india[i][filter1], filter2.upper(),
                                          covid_cases_india[i][filter2],
                                          filter3.upper(), covid_cases_india[i][filter3]))
    print(covid_data["statewise"][i]["lastupdatedtime"], )
    print("~~+~~++~~+~~++~~+~~++~~+~~++~~")
    print()
