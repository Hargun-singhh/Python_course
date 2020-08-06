import requests

import json


class Covid:
    def __init__(self, daily_date, daily_confirmed, daily_recovered, daily_deceased):
        self.daily_data = daily_date
        self.daily_confirmed = daily_confirmed
        self.daily_recovered = daily_recovered
        self.daily_deceased = daily_deceased

    def __str__(self):
        return "{} : {} : {} : {}\n".format(self.daily_data, self.daily_confirmed, self.daily_recovered, self.daily_deceased)


class fetchpundata:

    def fetch(self, save_data):

        url = "https://api.covid19india.org/data.json"
        response = requests.get(url)
        covid_data = json.loads(response.text)
        covid_data_daily = covid_data["cases_time_series"]
        i = 0
        covid_data_new = []
        covid_data_confirmed = []
        covid_data_recovered = []
        covid_data_deaths = []

        for i in range(0, len(covid_data_daily)):
            covid_data_new.append(covid_data_daily[i]["date"])

        for i in range(0, len(covid_data_daily)):
            covid_data_confirmed.append(covid_data_daily[i]["dailyconfirmed"])

        for i in range(0, len(covid_data_daily)):
            covid_data_recovered.append(covid_data_daily[i]["dailyrecovered"])

        for i in range(0, len(covid_data_daily)):
            covid_data_deaths.append(covid_data_daily[i]["dailydeceased"])

        covid_csv = []
        for i in range(0, len(covid_data_new)):
            data = Covid(covid_data_new[i], covid_data_confirmed[i], covid_data_recovered[i], covid_data_deaths[i])
            covid_csv.append(data)
        if save_data:
            file = open('COVID_DATA_DAILY.csv', 'a')
            for team in covid_csv:
                file.write(str(team))
            print("DATA-SAVED-IN-FILE")


def main():
    data = fetchpundata()
    data.fetch(True)


if __name__ == '__main__':
    main()
