import requests
import json
import matplotlib.pyplot as plt
url = "https://api.covid19india.org/data.json"

response = requests.get(url)
covid_data = json.loads(response.text)

covid_cases_cases= []
for i in range(0, len(covid_data["cases_time_series"])):
    covid_cases_cases.append(
        {
            "date": covid_data["cases_time_series"][i]["date"],
            "totalconfirmed": covid_data["cases_time_series"][i]["totalconfirmed"],
            "totaldeceased": covid_data["cases_time_series"][i]["totaldeceased"],
            "totalrecovered": covid_data["cases_time_series"][i]["totalrecovered"],
        }
    )
filter1 = input("Please Enter 1st Filter from [date | totalconfirmed | totaldeceased | totalrecovered ]: ")
filter2 = input("Please Enter 2nd Filter from [date | totalconfirmed | totaldeceased | totalrecovered ]: ")
filter3 = input("Please Enter 2nd Filter from [date | totalconfirmed | totaldeceased | totalrecovered ]: ")

for i in range(0, len(covid_cases_cases)):
    print("~~+~~++~~+~~++~~+~~++~~+~~++~~")
    print("{}: {}\n{}: {}\n{}: {}".format(filter1.upper(), covid_cases_cases[i][filter1], filter2.upper(),
                                          covid_cases_cases[i][filter2],
                                          filter3.upper(), covid_cases_cases[i][filter3]))
    print("~~+~~++~~+~~++~~+~~++~~+~~++~~")
    print()
total_confirmed = []
for case in covid_cases_cases:
    total_confirmed.append(int(case['totalrecovered']))

plt.plot(total_confirmed)
plt.show()


file = open("COVID19_DATA_DAILY_BASIS.csv", "a")
file.write(str(covid_data['cases_time_series']))
print("Data Saved according to day wise  :: )")
