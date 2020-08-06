import requests

import json


class Covid:
    def __init__(self, daily_data, daily_date, daily_confirmed, recovered, deaths):
        self.daily_data = daily_data
        self.daily_date = daily_date
        self.daily_confirmed = daily_confirmed
        self.recovered = recovered
        self.deaths = deaths

    def __str__(self):
        return "{} | {} | {} | {} | {}\n".format(self.daily_data, self.daily_date, self.daily_confirmed, self.recovered, self.deaths)


class fetchpundata:

    def fetch(self, save_data):

        url = "https://api.covid19india.org/data.json"
        response = requests.get(url)
        covid_data = json.loads(response.text)
        covid_data_daily = covid_data['statewise']
        i = 0
        covid_data_new = []
        covid_data_new_confirmed = []
        covid_data_new_active = []
        covid_data_recovered = []
        covid_data_deaths = []

        for i in range(0, len(covid_data_daily)):
            covid_data_new.append(covid_data_daily[i]["state"])

        for i in range(0, len(covid_data_daily)):
            covid_data_new_confirmed.append(covid_data_daily[i]["confirmed"])

        for i in range(0, len(covid_data_daily)):
            covid_data_new_active.append(covid_data_daily[i]["active"])

        for i in range(0, len(covid_data_daily)):
            covid_data_recovered.append(covid_data_daily[i]["recovered"])

        for i in range(0, len(covid_data_daily)):
            covid_data_deaths.append(covid_data_daily[i]["deaths"])

        covid_csv = []
        for i in range(0, len(covid_data_new)):
            data = Covid(covid_data_new[i], covid_data_new_confirmed[i], covid_data_new_active[i], covid_data_recovered[i], covid_data_deaths[i])
            covid_csv.append(data)
        if save_data:
            file = open('COVID_--DATA.csv', 'a')
            for team in covid_csv:
                file.write(str(team))
            print("DATA-SAVED-IN-FILE")


def main():
    data = fetchpundata()
    data.fetch(True)


if __name__ == '__main__':
    main()
