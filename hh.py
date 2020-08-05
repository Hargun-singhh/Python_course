import requests
from bs4 import BeautifulSoup


class covid:

    def __init__(self, state, confirmed, active, discharged, deaths):
        self.state = state
        self.Confirmed = confirmed
        self.Active = active
        self.Discharged = discharged
        self.Deaths = deaths

    def __str__(self):
        return "{},{},{},{},{}\n".format(
            self.state, self.Confirmed, self.Active, self.Discharged, self.Deaths)


class FetchcovidData:

    def fetchData(self, save_data):

        url = "https://www.mygov.in/covid-19"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        covid_name_tags = soup.find_all("span", class_="st_name")
        covid_data_tags = soup.find_all("div", class_="st_all_counts")

        covid_names = []
        covid_data = []

        for tag in covid_name_tags:
            covid_names.append(tag.text.strip())
            covid_data.append([])

        # represents list index in the list
        i = 0
        j = 0

        for tag in covid_data_tags:
            covid_data[i].append(str(tag.text.strip()))

            j += 1

            if j % 6 == 0:
                i += 1

        # print(len(team_names))
        # print(len(team_data))
        # print(len(team_points))

        teams = []

        for i in range(0, len(covid_names)):
            covid = (covid_names[i], covid_data[i], covid_data[i][1],
                         covid_data[i][2], covid_data[i][3])

            teams.append(covid)

        if save_data:
            file = open("COVID__--DATA.csv", 'a')

            for covid in teams:
                print(covid)
                file.write(str(covid))

            print("DATA-SAVED-IN-FILE")

        else:
            for team in teams:
                print(team)


def main():
    data = FetchcovidData()
    data.fetchData(True)


if __name__ == '__main__':
    main()
